import React, { useRef } from 'react';
import { Canvas, useFrame } from '@react-three/fiber';
import { Box } from '@react-three/drei';

const SpinningMesh: React.FC = () => {
  const meshRef = useRef<THREE.Mesh>(null!); // Using non-null assertion for simplicity here
  useFrame(() => {
    if (meshRef.current) {
      meshRef.current.rotation.x += 0.01;
      meshRef.current.rotation.y += 0.01;
    }
  });

  return (
    <Box ref={meshRef} args={[2, 2, 2]}>
      <meshStandardMaterial color="orange" />
    </Box>
  );
};

const Hero3D: React.FC = () => {
  return (
    <Canvas style={{ position: 'absolute', top: 0, left: 0, zIndex: 0 }} camera={{ position: [0, 0, 5], fov: 75 }}>
      <ambientLight intensity={0.5} />
      <pointLight position={[10, 10, 10]} />
      <SpinningMesh />
    </Canvas>
  );
};

export default Hero3D;
