from django import forms
from .models import QuizResponse

class QuizForm(forms.ModelForm):
    class Meta:
        model = QuizResponse
        fields = [
            'name', 'email',
            'question1', 'question2', 'question3', 'question4', 'question5', 
            'question6', 'question7', 'question8', 'question9', 'question10', 
            'question11', 'question12', 'question13', 'question14', 'question15', 
            'question16', 'question17', 'question18', 'question19', 'question20'
        ]
        widgets = {
            'question1': forms.RadioSelect(choices=[
                ('32', '32'),
                ('24', '24'),
                ('20', '20')
            ]),
            'question2': forms.RadioSelect(choices=[
                ('20 km/hr', '20 km/hr'),
                ('40 km/hr', '40 km/hr'),
                ('60 km/hr', '60 km/hr')
            ]),
            'question3': forms.RadioSelect(choices=[
                ('x = 4', 'x = 4'),
                ('x = 2', 'x = 2'),
                ('x = 1', 'x = 1')
            ]),
            'question4': forms.RadioSelect(choices=[
                ('28', '28'),
                ('17', '17'),
                ('15', '15')
            ]),
            'question5': forms.RadioSelect(choices=[
                ('1', '1'),
                ('2', '2'),
                ('3', '3')
            ]),
            'question6': forms.RadioSelect(choices=[
                ('To learn', 'To learn'),
                ('To earn', 'To earn'),
                ('Both', 'Both')
            ]),
            'question7': forms.RadioSelect(choices=[
                ('Overloading', 'Overloading'),
                ('Inheritance', 'Inheritance'),
                ('Polymorphism', 'Polymorphism')
            ]),
            'question8': forms.RadioSelect(choices=[
                ('Index', 'Index'),
                ('Key', 'Key'),
                ('Index and Key', 'Index and Key')
            ]),
            'question9': forms.RadioSelect(choices=[
                ('9', '9'),
                ('12', '12'),
                ('15', '15')
            ]),
            'question10': forms.RadioSelect(choices=[
                ('3 hours', '3 hours'),
                ('2 hours', '2 hours'),
                ('4 hours', '4 hours')
            ]),
            'question11': forms.RadioSelect(choices=[
                ('Honesty', 'Honesty'),
                ('Perseverance', 'Perseverance'),
                ('Both', 'Both')
            ]),
            'question12': forms.RadioSelect(choices=[
                ('GET and POST', 'GET and POST'),
                ('PUT and DELETE', 'PUT and DELETE'),
                ('All of the above', 'All of the above')
            ]),
            'question13': forms.RadioSelect(choices=[
                ('8', '8'),
                ('13', '13'),
                ('21', '21')
            ]),
            'question14': forms.RadioSelect(choices=[
                ('$40', '$40'),
                ('$30', '$30'),
                ('$50', '$50')
            ]),
            'question15': forms.RadioSelect(choices=[
                ('Manager', 'Manager'),
                ('CEO', 'CEO'),
                ('Leader', 'Leader')
            ]),
            'question16': forms.RadioSelect(choices=[
                ('SQL', 'SQL'),
                ('NoSQL', 'NoSQL'),
                ('Both', 'Both')
            ]),
            'question17': forms.RadioSelect(choices=[
                ('x = 7', 'x = 7'),
                ('x = 6', 'x = 6'),
                ('x = 8', 'x = 8')
            ]),
            'question18': forms.RadioSelect(choices=[
                ('50 cm²', '50 cm²'),
                ('60 cm²', '60 cm²'),
                ('100 cm²', '100 cm²')
            ]),
            'question19': forms.RadioSelect(choices=[
                ('Challenge', 'Challenge'),
                ('Solution', 'Solution'),
                ('Both', 'Both')
            ]),
            'question20': forms.RadioSelect(choices=[
                ('Inheritance', 'Inheritance'),
                ('Encapsulation', 'Encapsulation'),
                ('Polymorphism', 'Polymorphism')
            ])
        }

    def __init__(self, *args, **kwargs):
        super(QuizForm, self).__init__(*args, **kwargs)
        
        # Reasoning Questions
        self.fields['question1'].label = "Reasoning: What is the next number in the series: 2, 4, 8, 16, ?"
        self.fields['question2'].label = "Aptitude: If a train travels 20 km/hr faster than a car and both start from the same point and reach the same destination in the same time, how much faster is the train if the car takes 3 hours?"
        self.fields['question3'].label = "Reasoning: If 2x + 3 = 11, what is x?"
        self.fields['question4'].label = "Aptitude: What is the sum of the first 5 prime numbers?"

        # Personal Interview Questions
        self.fields['question5'].label = "Personal Interview: What is your approach to solving problems?"
        self.fields['question6'].label = "Personal Interview: Why do you want this job?"
        
        # Technical Questions
        self.fields['question7'].label = "Technical: Which of the following is a feature of polymorphism in OOP?"
        self.fields['question8'].label = "Technical: Which of the following helps to speed up database queries?"

        # Add labels for the remaining questions, grouped appropriately
        self.fields['question9'].label = "Reasoning: What is the result of 3 * 3 + 3?"
        self.fields['question10'].label = "Aptitude: If a car travels at 60 km/hr, how long will it take to travel 180 km?"
        self.fields['question11'].label = "Personal Interview: Which of the following best describes your work ethic?"
        self.fields['question12'].label = "Technical: Which HTTP methods are commonly used in REST APIs?"

        self.fields['question13'].label = "Reasoning: What is the next number in the sequence: 1, 1, 2, 3, 5, ?"
        self.fields['question14'].label = "Aptitude: If a product costs $50 and is on sale for 20% off, what is the sale price?"
        self.fields['question15'].label = "Personal Interview: Where do you see yourself in 5 years?"
        self.fields['question16'].label = "Technical: Which type of database is generally more scalable?"

        self.fields['question17'].label = "Reasoning: Solve for x: 2x - 4 = 10"
        self.fields['question18'].label = "Aptitude: If a rectangle has a length of 10 cm and a width of 5 cm, what is its area?"
        self.fields['question19'].label = "Personal Interview: Which of the following best describes how you handle challenges?"
        self.fields['question20'].label = "Technical: Which OOP concept is implemented by the code: `class B(A): pass`?"

