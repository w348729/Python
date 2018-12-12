

# assume this is python environment

class PersonalStatement(object):
    def __init__(self, property, status, company, job_title, job_description, my_goal):
        self.property = property
        self.status = status
        self.company = company
        self.job_title = job_title
        self.job_description = job_description
        self.goal = my_goal
        self.leisure_time = ''
        self.daily_task = []
        self.description = []
        self.it_journey = []

    @staticmethod
    def my_it_journey(it_journey):
        for each_journey in it_journey:
            print(each_journey)
        return 'list my it journey successfully'
        >>>'''
        'start my IT journey at the end of 2015 as I was obsessed for those those excellent website or mobile app, ' \
        'then I started to learn some basic knowledge by myself.In 2016, I heard System Analysis programme in ISS(NUS' \
        'Institution Of System Science) from internet and I decided to apply for it and successfully get a offer. ' \
        'So after 1 year of studying, I can officially telling others that I am programmer.Now I am working in Fintec' \
        'company as a back-end developer'
        '''
    def describe_myself(self):
        finish_journey = my_it_journey(self.it_journey)
        if finish_journey:
            print(self.description)
            return 'describe myself successfully'
        >>>'I believe I am a positive person who always can find out the affirmative side of things and constantly ' \
           'absorb new knowledge from people around me. My colleagues always say I am humorous and friendly person,' \
           'this two features help me to make to new friends during daily life. As I did not graduate from IT relevant ' \
           'major, so I paid much more effort and spend quite a lot of time to learn more and I believe that disadvantage' \
           'does not affect me right now. For the IT career, if you wanna be something in future, the most important one ' \
           'is you have to keep learning new stuff and get in contact with the latest technologies as the computer science' \
           'updating so significant fast.'
        else:
            return 'print IT journey first'

    @property
    def describe_leisure_time(self):
        # start to describe what usually I do in my leisure time
        if self.leisure_time:
            print(self.leisure_time)
            return 'description finished'
        >>>'In my daily life, I go work out almost every day to stay healthy and stay fit cause you know as a programmer,' \
           'you barely have to time to walk around in office, almost spend whole day in my chair. I do some reading almost ' \
           'every day, sometimes its about IT stuff, sometimes its could be a famous science fiction like Te Galactic Empire ' \
           'Trilogy from Isaac Asimov, known as the creator of the The Laws of Robotics. Currently, I am learning Angular' \
           'and some basic theory about machine learning. I believe the AI implementation in financial industry could cause ' \
           'huge impact, for example the AI system may recommend the best portfolio for user or calculate each trading ' \
           'risk base on massive historical data automatically. Even more, a online intelligent supporter can reply different' \
           'questions from all kinds of customers(some companies already have prototype for this kind application). As I ' \
           'know more about these knowledge, I believe it is the time for me to learn deeper.'


    @property
    def my_daily_task(self):
        if self.status:
            print('')
            return 'describe my daily tasks successfully'
        else:
            return 'failed'

    def describe_current_job(self):
        return ''



if __name__ == '__main__':
    property = {'name': 'wang ruixue', 'gender': 'male', 'birthday': '1990.05.04,', 'nationality': 'china'}
    status = 'working in sg'
    company = 'Mafint(fintech company in singapore)'
    job_title = 'backend developer'
    company_target = 'deliver a financial product'
    goal = 'going further in IT filed'
    it_journey = []
    daily_task = []
    description = ''

    me = PersonalStatement()

