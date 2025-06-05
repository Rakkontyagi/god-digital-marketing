import React, { useRef, useState } from 'react';
import { Canvas, useFrame } from '@react-three/fiber';
import { Box, Sphere, Text } from '@react-three/drei';
import * as THREE from 'three';

// Placeholder for India Map Geometry
const IndiaPlaceholderMesh: React.FC = () => {
  // A very simplified representation of India's rough shape for placeholder purposes
  // Imagine a stretched hexagon or a custom shape.
  // For simplicity, using a slightly flattened and scaled box.
  return (
    <Box args={[3, 4, 0.2]} rotation={[0, 0, Math.PI / 12]}>
      <meshStandardMaterial color="#228B22" transparent opacity={0.7} /> {/* Forest Green-ish */}
    </Box>
  );
};

const DelhiMarker: React.FC = () => {
  const meshRef = useRef<THREE.Mesh>(null!);
  const [hovered, setHover] = useState(false);
  const [clicked, setClick] = useState(false);

  useFrame(() => {
    if (meshRef.current && hovered) {
      // Optional: add subtle animation on hover
      // meshRef.current.rotation.y += 0.05;
    }
  });

  return (
    <Sphere
      ref={meshRef}
      args={[0.2, 32, 32]} // Small sphere for Delhi
      position={[-0.3, 0.5, 0.2]} // Approximate position on the placeholder map
      onPointerOver={(event) => { event.stopPropagation(); setHover(true);}}
      onPointerOut={(event) => setHover(false)}
      onClick={(event) => { event.stopPropagation(); setClick(!clicked);}}
    >
      <meshStandardMaterial color={hovered ? '#FF4500' : '#FF0000'} emissive={hovered ? '#FFA500' : '#FF0000'} emissiveIntensity={hovered ? 0.5: 0.2} />
      {/* Basic Text label - visibility might be an issue without proper setup */}
      {/* <Text position={[0, 0.3, 0]} fontSize={0.15} color="white" anchorX="center" anchorY="middle">
        Delhi
      </Text> */}
    </Sphere>
  );
};

const DelhiMap3D: React.FC = () => {
  return (
    <div style={{ height: '400px', width: '100%', background: 'rgba(0,0,50,0.3)' }}> {/* Added background to canvas container */}
      <Canvas camera={{ position: [0, 0, 5], fov: 50 }}>
        <ambientLight intensity={0.6} />
        <directionalLight position={[5, 5, 5]} intensity={1} />
        <IndiaPlaceholderMesh />
        <DelhiMarker />
        {/* OrbitControls can be added here for debugging model placement */}
        {/* <OrbitControls /> */}
      </Canvas>
    </div>
  );
};

export default DelhiMap3D;
