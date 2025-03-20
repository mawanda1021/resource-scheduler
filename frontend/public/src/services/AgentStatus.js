import React, { useState, useEffect } from 'react';
import socket from '../services/socket';

const AgentStatus = () => {
    const [agents, setAgents] = useState([]);

    useEffect(() => {
        socket.on("agent_status", (data) => {
            setAgents(data);
        });

        return () => {
            socket.off("agent_status");
        };
    }, []);

    return (
        <div>
            <h2>Agent Status</h2>
            {agents.map(agent => (
                <p key={agent.id}>
                    Agent {agent.id} - {agent.tasks.length} tasks assigned
                </p>
            ))}
        </div>
    );
};

export default AgentStatus;
