import React, { useState, useEffect } from 'react';
import socket from '../services/socket';

const Assignments = () => {
    const [assignments, setAssignments] = useState([]);

    useEffect(() => {
        socket.on("assignments", (data) => {
            setAssignments(data);
        });

        return () => {
            socket.off("assignments");
        };
    }, []);

    return (
        <div>
            <h2>Ongoing Assignments</h2>
            <ul>
                {assignments.map((assignment) => (
                    <li key={assignment.customer_id}>
                        Agent {assignment.agent_id} → Customer {assignment.customer_id}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default Assignments;
