import kue from 'kue';

const queue = kue.createQueue();
const blacklistedNumbers = ['4153518780', '4153518781'];

function sendNotification(phoneNumber, message, job, done) {
  job.progress(0, 100);
  
  if (blacklistedNumbers.includes(phoneNumber)) {
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }

  job.progress(50, 100);
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  done();
}

queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});

queue.on('job enqueue', (id, type) => {
  console.log(`Notification job #${id} 0% complete`);
});

queue.on('job complete', (id, result) => {
  console.log(`Notification job #${id} completed`);
});

queue.on('job failed', (id, errorMessage) => {
  console.log(`Notification job #${id} failed: ${errorMessage}`);
});

queue.on('job progress', (id, progress) => {
  console.log(`Notification job #${id} ${progress}% complete`);
});

