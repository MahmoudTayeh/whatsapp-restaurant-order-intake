import React, { useEffect, useState } from "react";
import axios from "axios";
import "./App.css";

interface OrderItem {
  id: number;
  item_name_snapshot: string;
  price_snapshot: string;
  quantity: number;
}

interface Order {
  id: number;
  order_number: string;
  restaurant_name: string;
  customer_phone: string;
  delivery_address: string;
  payment_method: string;
  total_amount: string;
  status: string;
  notes: string;
  created_at: string;
  items: OrderItem[];
}

function App() {
  const [orders, setOrders] = useState<Order[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchOrders = async () => {
      try {
        // In a real app, you'd handle authentication here
        const response = await axios.get("http://localhost:8000/api/orders/");
        setOrders(response.data);
      } catch (error) {
        console.error("Error fetching orders:", error);
      } finally {
        setLoading(false);
      }
    };

    fetchOrders();
    const interval = setInterval(fetchOrders, 10000); // Poll every 10 seconds
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>Restaurant Staff Dashboard</h1>
      </header>
      <main>
        {loading ? (
          <p>Loading orders...</p>
        ) : (
          <div className="order-list">
            {orders.length === 0 ? (
              <p>No orders yet.</p>
            ) : (
              orders.map((order) => (
                <div key={order.id} className={`order-card status-${order.status.toLowerCase()}`}>
                  <div className="order-header">
                    <h3>Order #{order.order_number}</h3>
                    <span className="status-badge">{order.status}</span>
                  </div>
                  <div className="order-details">
                    <p><strong>Customer:</strong> {order.customer_phone}</p>
                    <p><strong>Address:</strong> {order.delivery_address}</p>
                    <p><strong>Payment:</strong> {order.payment_method}</p>
                    <p><strong>Total:</strong> ${order.total_amount}</p>
                  </div>
                  <div className="order-items">
                    <h4>Items:</h4>
                    <ul>
                      {order.items.map((item) => (
                        <li key={item.id}>
                          {item.quantity} x {item.item_name_snapshot} (${item.price_snapshot})
                        </li>
                      ))}
                    </ul>
                  </div>
                  {order.notes && (
                    <div className="order-notes">
                      <p><strong>Notes:</strong> {order.notes}</p>
                    </div>
                  )}
                </div>
              ))
            )}
          </div>
        )}
      </main>
    </div>
  );
}

export default App;
