import React, { useEffect, useState } from 'react';
// import './index.css';

function App() {
  const [currentSlide, setCurrentSlide] = useState(0);
  const [orderStatus, setOrderStatus] = useState('');

  const slides = [
    <img src="/images/WhatsApp Image 2025-02-16 at 14.21.55_382dbf78.jpg" alt="Zula's Chicken Dish" />,
    <video autoPlay muted loop>
      <source src="/images/WhatsApp Video 2025-02-16 at 14.21.38_9cdaee3d.mp4" type="video/mp4" />
    </video>,
    <img src="/images/WhatsApp Image 2025-02-16 at 14.21.55_382dbf78.jpg" alt="Zula's Chicken Dish" />
  ];

  // Auto-slide logic
  useEffect(() => {
    const interval = setInterval(() => {
      setCurrentSlide((prev) => (prev + 1) % slides.length);
    }, 10000);
    return () => clearInterval(interval);
  }, [slides.length]);

  // Make a dynamic order via Flask API
  const makeOrder = async () => {
    const order = {
      customer_name: "Test User",
      phone: "0770000000",
      item: "Zula Chicken Box",
      quantity: 1
    };

    try {
      const response = await fetch('http://localhost:5000/orders', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(order)
      });

      const data = await response.json();
      setOrderStatus(`Order Placed! Order ID: ${data.id}`);
    } catch (error) {
      console.error('Order failed:', error);
      setOrderStatus("Order failed. Please try again later.");
    }
  };

  return (
    <div>
      {/* Navigation */}
      <nav>
        <ul>
          <li><a href="#home">Home</a></li>
          <li><a href="#menu">Menu</a></li>
          <li><a href="#ice-cream">Ice Cream</a></li>
          <li><a href="#contact">Contact Us</a></li>
        </ul>
      </nav>

      {/* Carousel */}
      <section id="home" className="carousel">
        <div className="carousel-container" style={{ transform: `translateX(-${currentSlide * 100}%)` }}>
          {slides.map((slide, index) => (
            <div className="carousel-item" key={index}>{slide}</div>
          ))}
        </div>
        <div className="order-button">
          <button onClick={makeOrder}>Make an Order</button>
          <p>{orderStatus}</p>
        </div>
      </section>

      {/* Contact Section */}
      <section id="contact">
        <h2>Contact Us</h2>
        <p>Location: Wandegeya, South Wing of the market.</p>
        <p>Call: 0759526488 / 0771240984 / 0758183018</p>
      </section>
    </div>
  );
}

export default App;




// import logo from './logo.svg';
// import './App.css';

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

// export default App;
