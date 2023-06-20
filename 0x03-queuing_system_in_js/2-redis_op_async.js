import { createClient, print } from 'redis';
import { promisify } from 'util';

const client = createClient();
client.on('connect', () => console.log('Redis client connected to the server'));

client.on('error', err => console.log(`Redis client not connected to the server: ${err}`));

const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, print);
};
const getRes = promisify(client.get).bind(client);

const displaySchoolValue = async (schoolName) => {
  const result = await getRes(schoolName).catch((error) => {
    if (error) {
      console.log(error);
      throw error;
    }
  });
  console.log(result);
};
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');