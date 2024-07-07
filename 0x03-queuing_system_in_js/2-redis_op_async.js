import redis from 'redis';
import { promisify } from 'util';

// Create a Redis client
const client = redis.createClient();

// Handle successful connection
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Handle connection errors
client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

/**
 * Sets a new value for a given school name in Redis.
 * @param {string} schoolName - The key to set.
 * @param {string} value - The value to set for the key.
 */
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

// Promisify the get function
const getAsync = promisify(client.get).bind(client);

/**
 * Displays the value of a given school name from Redis.
 * @param {string} schoolName - The key to retrieve.
 */
async function displaySchoolValue(schoolName) {
  try {
    const value = await getAsync(schoolName);
    console.log(value);
  } catch (err) {
    console.error(`Error retrieving value for ${schoolName}: ${err.message}`);
  }
}

// Display the value of 'Holberton'
displaySchoolValue('Holberton');

// Set a new value for 'HolbertonSanFrancisco' and then display it
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');

