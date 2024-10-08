import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.on('error', (err) => {
    console.log('Redis client not connected to the server:', err);
});

function createHash() {
    client.hset('HolbertonSchools', 'portland', 50, redis.print);
    client.hset('HolbertonSchools', 'Seattle', 80, redis.print);
    client.hset('HolbertonSchools', 'New York', 20, redis.print);
    client.hset('HolbertonSchools', 'Bogota', 20, redis.print);
    client.hset('HolbertonSchools', 'Cali', 40, redis.print);
    client.hset('HolbertonSchools', 'Paris', 2, redis.print);
}

function displayHash() {
    client.hgetall('HolbertonSchools', (err, value) => {
        if (err) {
            console.error('Error retrieving data:', err);
        } else {
            console.log(value);
        }
    });
}

createHash();
displayHash();