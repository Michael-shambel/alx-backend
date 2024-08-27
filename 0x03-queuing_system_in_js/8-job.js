export default function createPushNotificationsJobs(jobs, queue) {
    if (!(jobs instanceof Array)) {
        throw new Error('Jobs is not an array');
    }
    jobs.forEach((jobData) => {
        const job = queue.create('push_notification_code_3', jobData);
        job
            .on('enqueue', () => {
                console.log(`Notification job created: ${job.id}`);
            })
            .on('complete', () => {
                console.log(`Notification job ${job.id} completed`);
            })
            .on('failed', () => {
                console.log(`Notification job ${job.id} failed`);
            })
            .on('progress', (progress) => {
                console.log(`Notification job ${job.id} ${progress}% complete`);
            });
        job.save();

    });
}
