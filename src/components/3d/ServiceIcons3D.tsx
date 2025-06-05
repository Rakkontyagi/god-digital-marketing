import React, { useRef, useState, useMemo } from 'react';
import { Canvas, useFrame } from '@react-three/fiber';
import { Text, Box, Sphere, Torus, Dodecahedron, Cone } from '@react-three/drei';
import * as THREE from 'three';

interface FloatingIconProps {
  position: [number, number, number];
  color: string;
  shape: 'box' | 'sphere' | 'torus' | 'dodecahedron' | 'cone';
  serviceName: string;
  args?: any; // Arguments for the shape geometry
}

const FloatingIcon: React.FC<FloatingIconProps> = ({ position, color, shape, serviceName, args = [] }) => {
  const meshRef = useRef<THREE.Mesh>(null!);
  const textRef = useRef<any>(null!); // THREE.Object3D for Text
  const [hovered, setHover] = useState(false);
  const [active, setActive] = useState(false);

  // Bobbing animation
  useFrame(({ clock }) => {
    if (meshRef.current) {
      meshRef.current.rotation.y += 0.005; // Slow rotation
      meshRef.current.rotation.x += 0.003;
      meshRef.current.position.y = position[1] + Math.sin(clock.getElapsedTime() * 1.5 + position[0]) * 0.2; // Bobbing
    }
    if (textRef.current) {
        // Make text face camera
        // textRef.current.quaternion.copy(camera.quaternion);
        // This is more complex, Text from drei handles it by default if not part of the rotating mesh
    }
  });

  const geometry = useMemo(() => {
    switch (shape) {
      case 'sphere':
        return <Sphere args={args.length ? args : [0.5, 32, 32]}><meshStandardMaterial color={color} emissive={hovered ? color : 'black'} emissiveIntensity={hovered ? 0.5 : 0} /></Sphere>;
      case 'torus':
        return <Torus args={args.length ? args : [0.4, 0.15, 16, 100]}><meshStandardMaterial color={color} emissive={hovered ? color : 'black'} emissiveIntensity={hovered ? 0.5 : 0} /></Torus>;
      case 'dodecahedron':
        return <Dodecahedron args={args.length ? args : [0.5]}><meshStandardMaterial color={color} emissive={hovered ? color : 'black'} emissiveIntensity={hovered ? 0.5 : 0} /></Dodecahedron>;
      case 'cone':
        return <Cone args={args.length ? args : [0.4, 0.8, 32]}><meshStandardMaterial color={color} emissive={hovered ? color : 'black'} emissiveIntensity={hovered ? 0.5 : 0} /></Cone>;
      case 'box':
      default:
        return <Box args={args.length ? args : [0.7, 0.7, 0.7]}><meshStandardMaterial color={color} emissive={hovered ? color : 'black'} emissiveIntensity={hovered ? 0.5 : 0} /></Box>;
    }
  }, [shape, args, color, hovered]);

  return (
    <group position={position}>
      <mesh
        ref={meshRef}
        onPointerOver={(event) => { event.stopPropagation(); setHover(true);}}
        onPointerOut={(event) => setHover(false)}
        onClick={(event) => { event.stopPropagation(); setActive(!active);}}
        scale={active ? 1.2 : (hovered ? 1.1 : 1)}
      >
        {geometry}
      </mesh>
      { (hovered || active) && (
        <Text
          ref={textRef}
          position={[0, -0.8, 0]} // Position text below the icon
          fontSize={0.2}
          color="white"
          anchorX="center"
          anchorY="middle"
          outlineWidth={0.01}
          outlineColor="black"
        >
          {serviceName}
        </Text>
      )}
    </group>
  );
};

const ServiceIcons3D: React.FC = () => {
  const services = [
    { name: 'SEO & SEM', shape: 'sphere', color: '#FFD700', position: [-2.5, 0, 0], args: [0.5, 32, 32] }, // Gold
    { name: 'PPC Campaigns', shape: 'torus', color: '#32CD32', position: [-1, 0.2, 0], args: [0.4, 0.15, 16, 100] }, // LimeGreen
    { name: 'Social Media', shape: 'dodecahedron', color: '#1E90FF', position: [0.5, -0.1, 0], args: [0.5] }, // DodgerBlue
    { name: 'Web Design', shape: 'cone', color: '#FF69B4', position: [2, 0.1, 0], args: [0.4, 0.7, 32] }, // HotPink
  ];

  return (
    <div style={{ height: '300px', width: '100%', marginTop: '2rem', marginBottom: '1rem' }}>
      <Canvas camera={{ position: [0, 0.5, 5], fov: 50 }}>
        <ambientLight intensity={0.7} />
        <directionalLight position={[3, 5, 5]} intensity={1} />
        <pointLight position={[-3, -2, 4]} intensity={0.8} color="white" />

        {services.map(service => (
          <FloatingIcon
            key={service.name}
            position={service.position as [number, number, number]}
            color={service.color}
            shape={service.shape as any}
            serviceName={service.name}
            args={service.args}
          />
        ))}
        {/* <OrbitControls /> */}
      </Canvas>
    </div>
  );
};

export default ServiceIcons3D;
