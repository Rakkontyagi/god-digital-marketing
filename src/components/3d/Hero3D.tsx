import React, { useRef, useState } from 'react';
import { Canvas, useFrame } from '@react-three/fiber';
import { Box, Sphere, Torus, Dodecahedron, Environment } from '@react-three/drei'; // Removed Text
import * as THREE from 'three';
import { MeshPhysicalMaterialProps } from '@react-three/fiber'; // For types
import { EffectComposer, Bloom, DepthOfField } from '@react-three/postprocessing';
import { KernelSize } from 'postprocessing'; // KernelSize is used for Bloom effect

// Helper to create a transmissive material config
const getTransmissionMaterialProps = (): Partial<MeshPhysicalMaterialProps> => ({
  transmission: 1,
  thickness: 0.6, // Adjust for desired refraction
  roughness: 0.1,  // Low roughness for smooth glass
  ior: 1.5,        // Index of refraction for glass-like appearance
  // envMapIntensity: 1, // Requires an environment map to look best
  // clearcoat: 1,
  // clearcoatRoughness: 0.1,
});

const AnimatedShape: React.FC<{
  position: [number, number, number];
  initialRotation?: [number, number, number];
  color: string;
  shapeType: 'box' | 'sphere' | 'torus' | 'dodecahedron';
  animationParams: { rotX: number; rotY: number; bobSpeed?: number };
  isTransmissive?: boolean;
}> = ({ position, initialRotation = [0,0,0], color, shapeType, animationParams, isTransmissive = false }) => {
  const meshRef = useRef<THREE.Mesh>(null!);
  const [hovered, setHovered] = useState(false);

  useFrame(({ clock }) => {
    if (meshRef.current) {
      meshRef.current.rotation.x += animationParams.rotX;
      meshRef.current.rotation.y += animationParams.rotY;
      if (animationParams.bobSpeed) {
        meshRef.current.position.y = position[1] + Math.sin(clock.getElapsedTime() * animationParams.bobSpeed + position[0]) * 0.3;
      }
    }
  });

  const materialProps = isTransmissive ? getTransmissionMaterialProps() : {};

  let geometry;
  switch (shapeType) {
    case 'sphere':
      geometry = <sphereGeometry args={[0.7, 32, 32]} />;
      break;
    case 'torus':
      geometry = <torusGeometry args={[0.6, 0.2, 16, 100]} />;
      break;
    case 'dodecahedron':
      geometry = <dodecahedronGeometry args={[0.8]} />;
      break;
    case 'box':
    default:
      geometry = <boxGeometry args={[1, 1, 1]} />;
      break;
  }

  return (
    <mesh
      ref={meshRef}
      position={position}
      rotation={initialRotation}
      onPointerOver={(event) => { event.stopPropagation(); setHovered(true); }}
      onPointerOut={(event) => setHovered(false)}
      scale={hovered ? 1.1 : 1} // Apply scale effect
    >
      {geometry}
      {isTransmissive ? (
        <meshPhysicalMaterial
          color={color}
          {...materialProps}
        />
      ) : (
        <meshStandardMaterial color={color} roughness={0.3} metalness={0.1} />
      )}
    </mesh>
  );
};

const Hero3D: React.FC = () => {
  return (
    // Canvas is positioned absolutely by HeroSection's styling for Hero3D wrapper
    // zIndex is also handled by HeroSection's wrapper for Hero3D component
    <Canvas camera={{ position: [0, 1, 7], fov: 50 }} gl={{ antialias: true, pixelRatio: window.devicePixelRatio }}>
      {/* Original scene elements */}
      <ambientLight intensity={0.5} />
      <hemisphereLight intensity={0.3} groundColor="black" />
      <directionalLight position={[5, 8, 5]} intensity={1.2} castShadow />
      <pointLight position={[-5, -3, 2]} intensity={0.7} color="#FFFFFF" />

      {/* Main brand color shape - prominent */}
      <AnimatedShape
        position={[-1.5, 0.5, 0]}
        initialRotation={[0.2,0.5,0]}
        color="#f97316" // god-orange-DEFAULT
        shapeType="dodecahedron"
        animationParams={{ rotX: 0.0025, rotY: 0.0035, bobSpeed: 0.7 }}
      />

      {/* A secondary color shape, potentially transmissive */}
      <AnimatedShape
        position={[1.2, -0.2, -1]}
        initialRotation={[0.5,0.2,0.1]}
        color="#3b82f6" // god-blue-light
        shapeType="sphere"
        animationParams={{ rotX: 0.0035, rotY: 0.0025, bobSpeed: 0.5 }}
        isTransmissive={true} // Try transmission here
      />

      {/* A smaller accent shape */}
      <AnimatedShape
        position={[0.5, 1.5, -2]}
        initialRotation={[0.1,0.8,0.3]}
        color="#FFFFFF" // White or a very light accent
        shapeType="torus"
        animationParams={{ rotX: 0.0015, rotY: -0.0045, bobSpeed: 0.9 }}
      />

      {/* Another accent shape, different type */}
       <AnimatedShape
        position={[-0.8, -1.2, 0.5]}
        initialRotation={[0.6,0.1,0.7]}
        color="#DC143C" // delhi-red
        shapeType="box"
        animationParams={{ rotX: -0.0025, rotY: 0.0015, bobSpeed: 0.6 }}
      />

      {/* "city" preset provides good ambient reflections for metallic/glassy surfaces and general scenes. */}
      <Environment preset="city" />

      {/* Post-processing effects are applied here */}
      <EffectComposer>
        <Bloom
          intensity={0.6}
          kernelSize={KernelSize.SMALL}
          luminanceThreshold={0.7}
          luminanceSmoothing={0.025}
        />
        <DepthOfField
          focusDistance={0.02} // Distance to the point of focus
          focalLength={0.05} // Focal length of the virtual camera
          bokehScale={1.5} // Size of the bokeh blur
          height={480} // Resolution of the DoF effect, lower for performance
        />
      </EffectComposer>
      {/* <OrbitControls /> */}
    </Canvas>
  );
};

export default Hero3D;
