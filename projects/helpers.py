from projects.models import Project

def fill_projects():
    Project.objects.all().delete()

    Project.objects.create(
        title = 'Piazza Post Classifier',
        description = 'This project is an introductory machine learning project that trained a machine learning algorithm to classify ' \
        'Piazza posts by category. The goal of the project was to develop a tool that could automatically categorize Piazza posts based '\
        'on their content, making it easier for users to find relevant information and for instructors to track and manage course discussions.'\
        'To develop the classifier, the I collected a dataset of Piazza posts and their corresponding categories, and used this '\
        'dataset to train a machine learning algorithm.',
        tools_used = 'C++, Machine Learning, Natural Language Processing, Probability Theory, X-Code',
        img_name = 'img/piazzapic.png',
        created = True
    )

    Project.objects.create(
        title = 'Personal Website',
        description = 'This project is a personal portfolio website created by me to '\
        'showcase my skills, experience, and projects in both computer science and music. The website features a responsive design, '\
        'allowing it to be viewed on a variety of devices, including desktop computers, tablets, and smartphones.'\
        'The website includes a home page, a video gallery page, and a projects page. ',
        tools_used = 'Django Framework, Python, Web Development',
        img_name = 'img/websitepic.png',
        created = True
    )

    Project.objects.create(
        title = 'Album Ranker',
        description = 'This project is an in-progress web application that interacts with Spotify\'s REST API to build a web application '\
        'that allows users to search for an album and take a quiz based on the tracks of the album. The application includes an underlying '\
        'algorithm that uses the quiz answers to rank the album tracks based on the user\'s preference.',
        tools_used = 'Django Framework, Python, Web Development, REST API, Algorithm Theory',
        img_name = 'img/spotifyprojpic.png',
        created = True
    )
    
