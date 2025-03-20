import axios from 'axios';

const API_URL = 'http://localhost:5000';

export const getAgentStatus = async () => {
    return await axios.get(`${API_URL}/agents`);
};

export const getCustomerQueue = async () => {
    return await axios.get(`${API_URL}/queue`);
};

export const startScheduling = async (type) => {
    return await axios.post(`${API_URL}/start_scheduling`, { type });
};
