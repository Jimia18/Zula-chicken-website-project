// File: src/pages/Home.jsx
import React from 'react';
import './index.css'; // optional: extract styles if needed
import './image'

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

      {/* Carousel */}
      <section id="home" className="carousel">
        <div className="carousel-container">
          <div className="carousel-item">
            <img src="/images/60k.jpg" alt="Zula's Chicken Dish" />
          </div>
          <div className="carousel-item">
            <video autoPlay muted loop>
              <source src="/images/homescreenvideo.mp4" type="video/mp4" />
              <source src="/images/homescreenvideo.mp4" type="video/mp4" />
            </video>
          </div>
          <div className="carousel-item">
            <img src="/images/60k.jpg" alt="Zula's Chicken Dish" />
          </div>
        </div>

        {/* Order Button */}
        <div className="order-button">
          <p id="order"></p>
          <a href="/menu">
            <button>Make an Order</button>
          </a>
        </div>
      </section>

      {/* Contact Section */}
      <section id="contact">
        <h2>Contact Us</h2>
        <p>Location: Wandegeya, South Wing of the market at the extreme end.</p>
        <p>For inquiries, call: 0759526488 / 0771240984 /0758183018</p>
      </section>
    </div>
  );
}
