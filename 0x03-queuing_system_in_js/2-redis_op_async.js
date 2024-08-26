import { createClient } from "redis";
import { promisify } from 'util';
import redis from 'redis';

const client = createClient();

client.on('error', (err) => console.log('Redis client not connected to the server:', err));
client.on('connect', () => console.log('Redis client connected to the server'));

const getAsync = promisify(client.get).bind(client);

async function displaySchoolValue(schoolName) {
    try {
        const value = await getAsync(schoolName);
        console.log(value);
    } catch (err) {
        console.error('Error fetching value:', err);
    }
}

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, redis.print);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
