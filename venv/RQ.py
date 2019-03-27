from redis import Redis
from rq import use_connection, Queue, get_current_job, Connection, cancel_job
from rq.worker import Worker
from helpers import cocktailSort, make_list
import time
import sys
import os
import signal


redis = Redis('127.0.0.1', 6379, password='')
q = Queue(connection=redis)


workers = Worker.all(connection=redis)
print(workers)


def print_all_jobs():
    print(q.job_ids)

    jobs = q.job_ids
    for i in range(0, len(jobs)):
        print(q.fetch_job(jobs[i]).status)


def add_job(list_size, id):
    job = q.enqueue(cocktailSort, [make_list(list_size), [1,2,3,4]], job_id=id)
    if job is not None:
        print("New Job Added, Status: {}".format(job.status))
    else:
        print("Job not Queued")
    return job.id


def check_status(id):
    if id != "":
        current_job = q.fetch_job(id)
        if current_job is not None:
            print("Status of {}: {}".format(id, current_job.status))
            return current_job.status
        else:
            return "Job ID does not exist"
    else:
        return "Enter a Job ID"


def cancel_job(id):
    print("Attempting To Cancel...")
    job = q.fetch_job(id)
    if job is not  None:
        if job.status == "finished":
            return "Job has already completed"
        elif job.status == "started":
            w = Worker.all(connection=redis)
            for worker in w:
                j = worker.get_current_job()
                if j.id == job.id:
                    result = worker.key.split('.')
                    os.kill(int(result[1]), signal.SIGKILL)
                    print("OS KILL: {}".format(worker.pid))
        else:
            job.delete()
            return "Cancelled"
    else:
        return "Job Id does not exist"


def check_results(id):
    job = q.fetch_job(id)
    if job is not None:
        if job.status == "finished":
            print("Job Results: {}".format(job.result))
            result = job.result
            start_time = job.started_at
            end_time = job.ended_at
            runtime = end_time - start_time
            results = "Start time: {}<br>End time: {}<br> Run time: {}<br>Result: {}".format(start_time, end_time, runtime, result)
            return results
        else:
            return "Running"
    else:
        return "Job ID does not exist"


# job_0 = q.enqueue(cocktailSort, make_list(100))
# job_1 = q.enqueue(cocktailSort, make_list(1000))
# job_2 = q.enqueue(cocktailSort, make_list(500))
# job_3 = q.enqueue(cocktailSort, make_list(50))
# job_4 = q.enqueue(cocktailSort, make_list(10000))
# time.sleep(5)
# job_IDS = q.job_ids
# print("Job IDS: {}".format(job_IDS))
#
# print("Job {}: {}".format(job_IDS[0], q.fetch_job(job_IDS[0])))
# print("Job 4 status: {}".format(job_1.status))
# time.sleep(1)
# print("Job 4 status: {}".format(job_1.status))
# time.sleep(1)
# print("Job 4 status: {}".format(job_1.status))
# time.sleep(1)
# print("Job 4 status: {}".format(job_1.status))
# time.sleep(1)
# print("Job 4 status: {}".format(job_1.status))
# time.sleep(1)
# print("Job 4 status: {}".format(job_1.status))
# time.sleep(1)
# print("Job 4 status: {}".format(job_1.status))
# time.sleep(1)
#
# print("Job 0: {}".format(job_0.result))
# print("Job 1: {}".format(job_1.result))
# print("Job 2: {}".format(job_2.result))
# print("Job 3: {}".format(job_3.result))
# print("Job 4: {}".format(job_4.result))
#
# print("Job 4 status: {}".format(job_1.status))
#
# print("Job 4 started at: {}".format(job_1.started_at)) # only returns None
# print("Job 4 ended at: {}".format(job_1.ended_at)) # only returns None
# q.delete(delete_jobs=True) # deletes all jobs in the queue
