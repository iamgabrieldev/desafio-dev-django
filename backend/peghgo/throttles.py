from rest_framework.throttling import AnonRateThrottle

class ResumeAnonRateThrottle(AnonRateThrottle):
    rate = '5/day'
    
class CandidateThrottle(AnonRateThrottle):
    rate = '10/day'