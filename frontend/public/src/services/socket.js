import { io } from "socket.io-client";

const socket = io("http://localhost:5000"); // Flask Server URL

export default socket;
