import React from 'react';
import AgentStatus from './components/AgentStatus';
import CustomerQueue from './components/CustomerQueue';
import Assignments from './components/Assignments';
import SchedulerControl from './components/SchedulerControl';

function App() {
    return (
        <div>
            <h1>Resource Scheduler Monitoring</h1>
            <SchedulerControl />
            <AgentStatus />
            <CustomerQueue />
            <Assignments />
        </div>
    );
}

export default App;
