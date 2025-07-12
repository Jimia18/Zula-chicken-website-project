// File: src/pages/Home.jsx
import React from 'react';
import '../styles/IceCream.css'; // optional: extract styles if needed

export default function Home() {
  return (
    <div>
      {/* Navigation Bar */}
      <nav>
        <ul>
          <li><a href="/">Home</a></li>
          <li><a href="/menu">Menu</a></li>
          <li><a href="/about">About us</a></li>
          <li><a href="/icecream">Ice Cream Point</a></li>
          <li><a href="/contact">Contact Us</a></li>
        </ul>
      </nav>
    </div>
  );
}

