from .models import State
ALLOWED = {
 State.DISCOVERED.value:{State.RIGHTS_CHECK.value,State.REJECTED_RIGHTS.value},
 State.RIGHTS_CHECK.value:{State.READY.value,State.REJECTED_RIGHTS.value,State.RETRY_WAIT.value},
 State.READY.value:{State.PROCESSING.value,State.RETRY_WAIT.value},
 State.PROCESSING.value:{State.VALIDATING.value,State.RETRY_WAIT.value,State.FAILED.value},
 State.VALIDATING.value:{State.READY_TO_PUBLISH.value,State.RETRY_WAIT.value,State.FAILED.value},
 State.READY_TO_PUBLISH.value:{State.PUBLISHING.value,State.RETRY_WAIT.value},
 State.PUBLISHING.value:{State.PUBLISHED.value,State.RETRY_WAIT.value,State.FAILED.value},
 State.RETRY_WAIT.value:{State.READY.value,State.PROCESSING.value,State.PUBLISHING.value,State.FAILED.value},
 State.PUBLISHED.value:set(), State.REJECTED_RIGHTS.value:set(), State.FAILED.value:set()
}
def transition(job, target):
    if target not in ALLOWED.get(job.state,set()):
        raise ValueError(f"Illegal job transition {job.state} -> {target}, job={job.job_id}")
    job.state=target; return job
