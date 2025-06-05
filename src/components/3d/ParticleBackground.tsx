import React, { useMemo, useRef } from 'react';
import { Canvas, useFrame } from '@react-three/fiber';
import * as THREE from 'three';

interface ParticleBackgroundProps {
  count?: number;
  color?: string;
  size?: number;
  speed?: number;
}

const Particles: React.FC<ParticleBackgroundProps> = ({
  count = 5000,
  color = '#FFFFFF',
  size = 0.015,
  speed = 0.1
}) => {
  const pointsRef = useRef<THREE.Points>(null!);

  const particles = useMemo(() => {
    const positions = new Float32Array(count * 3);
    for (let i = 0; i < count * 3; i++) {
      // Distribute particles in a sphere-like volume
      const r = Math.random() * 4 + 1; // Radius between 1 and 5
      const theta = Math.random() * Math.PI * 2;
      const phi = Math.acos((Math.random() * 2) - 1);
      positions[i * 3 + 0] = r * Math.sin(phi) * Math.cos(theta); // x
      positions[i * 3 + 1] = r * Math.sin(phi) * Math.sin(theta); // y
      positions[i * 3 + 2] = r * Math.cos(phi);                   // z
    }
    return positions;
  }, [count]);

  useFrame(({ clock }) => {
    if (pointsRef.current) {
      // Subtle animation: slow rotation or drift
      pointsRef.current.rotation.y += clock.getDelta() * speed * 0.1;
      pointsRef.current.rotation.x += clock.getDelta() * speed * 0.05;
    }
  });

  return (
    <points ref={pointsRef}>
      <bufferGeometry attach="geometry">
        <bufferAttribute
          attach="attributes-position"
          array={particles}
          count={particles.length / 3}
          itemSize={3}
        />
      </bufferGeometry>
      <pointsMaterial
        attach="material"
        size={size}
        color={color}
        sizeAttenuation={true}
        transparent={true}
        opacity={0.7}
        blending={THREE.AdditiveBlending} // Brighter effect for overlapping particles
      />
    </points>
  );
};

const ParticleBackground: React.FC<ParticleBackgroundProps> = (props) => {
  return (
    <div style={{ position: 'absolute', top: 0, left: 0, width: '100%', height: '100%', zIndex: -1 }}> {/* Ensure it's behind other content */}
      <Canvas
        camera={{ position: [0, 0, 1], fov: 75 }}
        gl={{ antialias: true, pixelRatio: (typeof window !== 'undefined' ? window.devicePixelRatio : 1) }}
      >
        <Particles {...props} />
      </Canvas>
    </div>
  );
};

export default ParticleBackground;
