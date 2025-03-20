import React from 'react';
import { startScheduling } from '../services/api';

const SchedulerControl = () => {
    const handleStart = async (type) => {
        await startScheduling(type);
        alert(`${type} scheduling started!`);
    };

    return (
        <div>
            <h2>Scheduler Control</h2>
            <button onClick={() => handleStart("round_robin")}>Round Robin</button>
            <button onClick={() => handleStart("priority")}>Priority</button>
            <button onClick={() => handleStart("shortest_job_next")}>Shortest Job Next</button>
        </div>
    );
};

export default SchedulerControl;
