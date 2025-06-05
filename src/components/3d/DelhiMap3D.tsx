import React, { useRef, useState, useMemo } from 'react'; // Removed useEffect
import { Canvas, useFrame } from '@react-three/fiber';
import { Sphere, Text, Environment, Extrude } from '@react-three/drei';
import * as THREE from 'three';

// Component for India's Shape Geometry
const IndiaShapeGeometry: React.FC = () => {
  const indiaShape = useMemo(() => {
    // Path for a VERY simplified outline of India.
    // Coordinates are normalized and may require adjustment for visual accuracy.
    const shape = new THREE.Shape();
    // Top part (Kashmir region)
    shape.moveTo(0, 2);
    shape.lineTo(0.5, 1.5);
    shape.lineTo(0.2, 1);
    // West coast
    shape.lineTo(-0.5, 0);
    shape.lineTo(-0.8, -1);
    // Southern tip
    shape.lineTo(0, -2);
    // East coast
    shape.lineTo(0.8, -1);
    shape.lineTo(0.5, 0);
    // Connecting to top-east
    shape.lineTo(0.7, 1);
    shape.lineTo(0.3, 1.5);
    shape.closePath(); // Close path back to (0, 2)
    return shape;
  }, []);

  return (
    <mesh rotation={[-Math.PI / 18, 0, Math.PI / 24]} scale={[1,1,1]}> {/* Slight tilt and rotation */}
      <extrudeGeometry args={[indiaShape, { depth: 0.1, bevelEnabled: false }]} />
      <meshStandardMaterial color="#2E8B57" emissive="#10502F" emissiveIntensity={0.3} roughness={0.7} metalness={0.2} />
    </mesh>
  );
};

const DelhiMarker: React.FC = () => {
  const meshRef = useRef<THREE.Group>(null!); // Changed to Group
  const [hovered, setHover] = useState(false);
  const [clicked, setClick] = useState(false); // Keep click for future

  // Bobbing animation for the marker
  useFrame(({ clock }) => {
    if (meshRef.current) {
      // Using 0.6 as the base Y position for bobbing, as per the new position
      meshRef.current.position.y = (0.6) + Math.sin(clock.getElapsedTime() * 2 + 0.1) * 0.05;
    }
  });

  return (
    // Position is set on the group, including the base Y for bobbing
    <group ref={meshRef} position={[0.1, 0.6, 0.15]} >
      <Sphere
        args={[0.12, 32, 32]} // Slightly smaller marker
        onPointerOver={(event) => { event.stopPropagation(); setHover(true);}}
        onPointerOut={(event) => setHover(false)}
        onClick={(event) => { event.stopPropagation(); setClick(!clicked);}}
        scale={clicked ? 1.5 : 1} // Scale effect on click
      >
        <meshStandardMaterial color={hovered ? '#FF4500' : '#FF0000'} emissive={hovered ? '#FFA500' : '#FF0000'} emissiveIntensity={hovered ? 0.8 : 0.4} />
      </Sphere>
      { (hovered || clicked) && (
        <Text position={[0, 0.25, 0]} fontSize={0.1} fontWeight="bold" color="white" outlineWidth={0.005} outlineColor="#222222" anchorX="center" anchorY="middle">
          DELHI
        </Text>
      )}
    </group>
  );
};

const DelhiMap3D: React.FC = () => {
  return (
    <div style={{ height: '450px', width: '100%', background: 'transparent' }}>
      <Canvas camera={{ position: [0, 0.5, 3.5], fov: 50 }} gl={{ antialias: true, pixelRatio: (typeof window !== 'undefined' ? window.devicePixelRatio : 1) }}>
        <ambientLight intensity={0.3} />
        <directionalLight position={[5, 5, 5]} intensity={0.6} />
        {/* "dawn" preset provides soft, neutral lighting suitable for a map display. */}
        <Environment preset="dawn" />
        <IndiaShapeGeometry />
        <DelhiMarker />
        {/* OrbitControls can be added here for debugging model placement */}
        {/* <OrbitControls /> */}
      </Canvas>
    </div>
  );
};

export default DelhiMap3D;
