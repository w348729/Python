

# assume this is python environment

class PersonalStatement(object):
    def __init__(self, property, status, my_description, company, job_title, job_description, my_goal, leisure_time,
                 it_journey):
        self.property = property
        self.status = status
        self.my_description = my_description
        self.company = company
        self.job_title = job_title
        self.job_description = job_description
        self.my_goal = my_goal
        self.leisure_time = leisure_time
        self.it_journey = it_journey

    def get_property(self):
        for each in property:
            print(each)

    def my_it_journey(self):
        for each_journey in self.it_journey:
            print(each_journey)
        return 'list my it journey successfully'
        >>>'start my IT journey at the end of 2015 as I was obsessed for those those excellent ' \
           'website or mobile app,then I started to learn some basic knowledge by myself.In 2016,' \
           ' I heard System Analysis programme in ISS(NUS Institution Of System Science) from ' \
           'internet and I decided to apply for it and successfully get a offer.So after 1 year ' \
           'of studying, I can officially telling others that I am programmer.Now I am working in Fintec' \
           'company as a back-end developer'

    def describe_myself(self):
        finish_journey = my_it_journey(self.it_journey)
        if finish_journey:
            if self.description:
                print(self.description)
                return 'describe myself successfully'
        >>>'I believe I am a positive person who always can find out the affirmative side of things ' \
           'and constantly absorb new knowledge from people around me. My colleagues always say I am ' \
           'humorous and friendly person,this two features help me to make to new friends during daily ' \
           'life. As I did not graduate from IT relevant major, so I paid much more effort and spend ' \
           'quite a lot of time to learn more and I believe that disadvantage does not affect me right ' \
           'now. For the IT career, if you wanna be something in future, the most important one ' \
           'is you have to keep learning new stuff and get in contact with the latest technologies as ' \
           'the computer science updating so significant fast.'
        else:
            return 'print IT journey first'

    def describe_leisure_time(self):
        # start to describe what usually I do in my leisure time
        if self.leisure_time:
            print(self.leisure_time)
            return 'description finished'
        >>>'In my daily life, I go work out almost every day to stay healthy and stay fit cause you ' \
           'know as a programmer, you barely have to time to walk around in office, almost spend whole ' \
           'day in my chair. I do some reading almost every day, sometimes its about IT stuff, sometimes ' \
           'its could be a famous science fiction like Te Galactic Empire Trilogy from Isaac Asimov, known' \
           'as the creator of the The Laws of Robotics. Besides, I like drawing very much, I draw somthine ' \
           'like sketch every week, I put some of my work in the mail. Currently, I am learning Angular and ' \
           'some basic theory about machine learning. I believe the AI implementation in financial industry ' \
           'could cause  huge impact, for example the AI system may recommend the best portfolio for user or ' \
           'calculate each  trading risk base on massive historical data automatically. Even more, a online ' \
           'intelligent supporter which can reply different questions from all kinds of customers. As I know ' \
           'more about these knowledge I realize that I am so tiny in the deep endless sea of computer science,' \
           ' I believe it is the time for me to learn deeper.'


    def current_job_description(self):
        if self.status:
            above_decription_finished = True
            if above_decription_finished:
                print(self.description)
                return 'describe my daily tasks successfully'
        else:
            return 'failed'
        >>>'I mainly work on the backend stuff now, including develop API interface for project, take a part ' \
           'in designin the database and maintain it, develop and optimize finance relevant algorithm. ' \
           'Some times, I also need to maintain the meta data which retrieved from Exchange Center, ' \
           'basically its like we grab or buy the data from them, ' \
           'then convert them the format which we are using. As I work for backend,so I need cooperate ' \
           'quite a lot with frontend to satisfy their requirements for the  response. I always follow ' \
           'a rule for my development, keep my codes clean, readable, neat, so that it will be' \
           'much easier to maintain, even when you leave the company, others can take it over smoothly '

    def list_my_goal(self):
        for each in self.goal:
            print(each)
        >>>'1. being a professional programmer, not someone who can just develop some business logic, ' \
               'but also focus on developing advanced algorithm and constantly optimize system.' \
           '2. I wanna go deeper and further , so I wanna learn more about AI or machine learning' \
           '3. someday I will try to be a product manager who equipped by professional technical ' \
               'knowledge not someone who only do paper talk'

def personal_statement_complete(count):
    if count > 0:
        print('Thank very much for your time to read this')
        return 'Wish you have a good day'
    else:
        return 'Automatically print above contents.... '



if __name__ == '__main__':
    property = {'name': 'wang ruixue', 'gender': 'male', 'birthday': '1990.05.04,', 'nationality': 'china'}
    status = 'working in sg'
    my_description = ['...']
    company = 'Mafint(fintech company in singapore)'
    job_title = 'backend developer'
    job_description = 'long text here...'
    my_goal = ['...']
    it_journey = 'long text here...'
    leiture_time = 'long text here...'
    daily_task = 'long text here...'

    step_count = 0
    me = PersonalStatement(property, status, company, my_description, job_title, job_description, my_goal,
                           it_journey, leiture_time, daily_task)
    me.get_property()
    me.my_it_journey()
    me.describe_myself()
    me.describe_leisure_time()
    me.list_my_goal()
    step_count += 1
    personal_statement_complete(step_count)