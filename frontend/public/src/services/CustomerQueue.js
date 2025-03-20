import React, { useState, useEffect } from 'react';
import socket from '../services/socket';

const CustomerQueue = () => {
    const [queue, setQueue] = useState([]);

    useEffect(() => {
        socket.on("customer_queue", (data) => {
            setQueue(data);
        });

        return () => {
            socket.off("customer_queue");
        };
    }, []);

    return (
        <div>
            <h2>Customer Queue</h2>
            <ul>
                {queue.map((customer) => (
                    <li key={customer.customer_id}>
                        Customer {customer.customer_id} - Priority {customer.priority}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default CustomerQueue;
