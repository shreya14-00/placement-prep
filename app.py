import streamlit as st
import random
import time

# Page config
st.set_page_config(page_title="Placement Prep", page_icon="🎯", layout="wide")

# Load CSS from file
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Question Banks
QUESTION_BANKS = {
    "FY": {
        "Easy": {
            "Quantitative Aptitude": [
                {"question": "What is 10 + 15?", "options": ["20", "25", "30", "35"], "answer": "25", "explanation": "10 + 15 = 25"},
                {"question": "What is 5 × 6?", "options": ["25", "30", "35", "40"], "answer": "30", "explanation": "5 × 6 = 30"},
                {"question": "What is 100 - 45?", "options": ["45", "50", "55", "60"], "answer": "55", "explanation": "100 - 45 = 55"},
                {"question": "What is 50% of 100?", "options": ["25", "50", "75", "100"], "answer": "50", "explanation": "50% of 100 = 50"},
                {"question": "What is 12 ÷ 3?", "options": ["3", "4", "5", "6"], "answer": "4", "explanation": "12 ÷ 3 = 4"},
                {"question": "What is 20 + 30?", "options": ["40", "50", "60", "70"], "answer": "50", "explanation": "20 + 30 = 50"},
                {"question": "What is 15 - 7?", "options": ["6", "7", "8", "9"], "answer": "8", "explanation": "15 - 7 = 8"},
                {"question": "What is 9 × 9?", "options": ["72", "81", "90", "99"], "answer": "81", "explanation": "9 × 9 = 81"},
                {"question": "What is 100 ÷ 10?", "options": ["5", "10", "15", "20"], "answer": "10", "explanation": "100 ÷ 10 = 10"},
                {"question": "What is 25% of 200?", "options": ["25", "50", "75", "100"], "answer": "50", "explanation": "25% of 200 = 50"}
            ],
            "Logical Reasoning": [
                {"question": "Find next: 2, 4, 6, 8, ?", "options": ["9", "10", "11", "12"], "answer": "10", "explanation": "Even numbers series"},
                {"question": "Odd one out: Apple, Banana, Carrot, Orange", "options": ["Apple", "Banana", "Carrot", "Orange"], "answer": "Carrot", "explanation": "Carrot is vegetable"},
                {"question": "If today is Monday, what day after 2 days?", "options": ["Tuesday", "Wednesday", "Thursday", "Friday"], "answer": "Wednesday", "explanation": "Monday + 2 = Wednesday"},
                {"question": "Complete: 1, 3, 5, 7, ?", "options": ["8", "9", "10", "11"], "answer": "9", "explanation": "Odd numbers"},
                {"question": "Book is to Reading as Fork is to?", "options": ["Cooking", "Eating", "Kitchen", "Spoon"], "answer": "Eating", "explanation": "Tool and use"},
                {"question": "Find next: 5, 10, 15, 20, ?", "options": ["22", "25", "28", "30"], "answer": "25", "explanation": "Multiples of 5"},
                {"question": "Odd one: Red, Blue, Green, Apple", "options": ["Red", "Blue", "Green", "Apple"], "answer": "Apple", "explanation": "Apple is fruit"},
                {"question": "If yesterday was Sunday, what is today?", "options": ["Monday", "Saturday", "Sunday", "Tuesday"], "answer": "Monday", "explanation": "Day after Sunday"},
                {"question": "Complete: 10, 20, 30, 40, ?", "options": ["45", "50", "55", "60"], "answer": "50", "explanation": "Multiples of 10"},
                {"question": "Pen is to Write as Knife is to?", "options": ["Sharp", "Cut", "Metal", "Kitchen"], "answer": "Cut", "explanation": "Tool function"}
            ],
            "Verbal Ability": [
                {"question": "Synonym of 'HAPPY':", "options": ["Sad", "Joyful", "Angry", "Tired"], "answer": "Joyful", "explanation": "Same meaning"},
                {"question": "Antonym of 'BIG':", "options": ["Large", "Huge", "Small", "Giant"], "answer": "Small", "explanation": "Opposite"},
                {"question": "Plural of 'CAT':", "options": ["Cats", "Cates", "Catten", "Caties"], "answer": "Cats", "explanation": "Add 's'"},
                {"question": "Past tense of 'GO':", "options": ["Goed", "Gone", "Went", "Going"], "answer": "Went", "explanation": "Go-Went-Gone"},
                {"question": "Fill: He ___ to school.", "options": ["go", "goes", "going", "gone"], "answer": "goes", "explanation": "Third person"},
                {"question": "Synonym of 'FAST':", "options": ["Slow", "Quick", "Late", "Early"], "answer": "Quick", "explanation": "Same meaning"},
                {"question": "Antonym of 'HOT':", "options": ["Warm", "Cold", "Boiling", "Burning"], "answer": "Cold", "explanation": "Opposite"},
                {"question": "Plural of 'BOX':", "options": ["Boxs", "Boxes", "Boxen", "Boxies"], "answer": "Boxes", "explanation": "Add 'es'"},
                {"question": "Past tense of 'EAT':", "options": ["Eated", "Eaten", "Ate", "Eating"], "answer": "Ate", "explanation": "Eat-Ate-Eaten"},
                {"question": "Fill: They ___ playing.", "options": ["is", "are", "was", "been"], "answer": "are", "explanation": "Plural subject"}
            ],
            "Technical (CS/IT)": [
                {"question": "What does CPU stand for?", "options": ["Central Process Unit", "Central Processing Unit", "Computer Personal Unit", "Central Processor Unit"], "answer": "Central Processing Unit", "explanation": "CPU is brain"},
                {"question": "Which is programming language?", "options": ["HTML", "Python", "CSS", "HTTP"], "answer": "Python", "explanation": "Python is language"},
                {"question": "1 Byte equals?", "options": ["4 bits", "8 bits", "16 bits", "32 bits"], "answer": "8 bits", "explanation": "1 Byte = 8 bits"},
                {"question": "Which is input device?", "options": ["Monitor", "Printer", "Keyboard", "Speaker"], "answer": "Keyboard", "explanation": "Keyboard gives input"},
                {"question": "Binary of 5?", "options": ["100", "101", "110", "111"], "answer": "101", "explanation": "5 = 101"},
                {"question": "Full form of RAM?", "options": ["Random Access Memory", "Read Access Memory", "Run Access Memory", "Real Access Memory"], "answer": "Random Access Memory", "explanation": "RAM is volatile"},
                {"question": "Which is output device?", "options": ["Mouse", "Keyboard", "Monitor", "Scanner"], "answer": "Monitor", "explanation": "Monitor shows output"},
                {"question": "1 KB equals?", "options": ["1000 bytes", "1024 bytes", "2048 bytes", "512 bytes"], "answer": "1024 bytes", "explanation": "1 KB = 1024 bytes"},
                {"question": "Which is brain of computer?", "options": ["RAM", "CPU", "ROM", "Hard Disk"], "answer": "CPU", "explanation": "CPU processes"},
                {"question": "Binary of 10?", "options": ["1000", "1001", "1010", "1011"], "answer": "1010", "explanation": "10 = 1010"}
            ]
        },
        "Medium": {
            "Quantitative Aptitude": [
                {"question": "What is 15% of 200?", "options": ["20", "25", "30", "35"], "answer": "30", "explanation": "15% of 200 = 30"},
                {"question": "If 2x + 3 = 11, find x.", "options": ["3", "4", "5", "6"], "answer": "4", "explanation": "2x = 8, x = 4"},
                {"question": "Average of 10, 20, 30?", "options": ["15", "20", "25", "30"], "answer": "20", "explanation": "(10+20+30)/3 = 20"},
                {"question": "What is 3/4 as percentage?", "options": ["65%", "70%", "75%", "80%"], "answer": "75%", "explanation": "3/4 = 75%"},
                {"question": "SI on Rs.1000 at 10% for 1 year?", "options": ["Rs.50", "Rs.100", "Rs.150", "Rs.200"], "answer": "Rs.100", "explanation": "SI = 100"},
                {"question": "What is 20% of 500?", "options": ["50", "75", "100", "125"], "answer": "100", "explanation": "20% of 500 = 100"},
                {"question": "If 3x = 15, find x.", "options": ["3", "4", "5", "6"], "answer": "5", "explanation": "x = 5"},
                {"question": "Average of 5, 10, 15, 20?", "options": ["10", "12.5", "15", "17.5"], "answer": "12.5", "explanation": "50/4 = 12.5"},
                {"question": "What is 2/5 as percentage?", "options": ["30%", "35%", "40%", "45%"], "answer": "40%", "explanation": "2/5 = 40%"},
                {"question": "SI on Rs.2000 at 5% for 2 years?", "options": ["Rs.100", "Rs.200", "Rs.300", "Rs.400"], "answer": "Rs.200", "explanation": "SI = 200"}
            ],
            "Logical Reasoning": [
                {"question": "Complete: 5, 10, 20, 40, ?", "options": ["60", "70", "80", "90"], "answer": "80", "explanation": "×2 each time"},
                {"question": "RED → TGF, BLUE → ?", "options": ["CNWF", "DMXF", "DNWF", "ENXF"], "answer": "DNWF", "explanation": "+2 shift"},
                {"question": "Circle is to Sphere as Square is to?", "options": ["Rectangle", "Cube", "Triangle", "Pyramid"], "answer": "Cube", "explanation": "2D to 3D"},
                {"question": "Find odd: 2, 3, 5, 9", "options": ["2", "3", "5", "9"], "answer": "9", "explanation": "Not prime"},
                {"question": "If all A are B, all B are C, then?", "options": ["All A are C", "Some A are C", "No A are C", "None"], "answer": "All A are C", "explanation": "Transitive"},
                {"question": "Complete: 3, 6, 12, 24, ?", "options": ["36", "42", "48", "54"], "answer": "48", "explanation": "×2"},
                {"question": "CAT → DBU, DOG → ?", "options": ["EPH", "EQH", "FPH", "EPG"], "answer": "EPH", "explanation": "+1 shift"},
                {"question": "Square is to Four as Triangle is to?", "options": ["Two", "Three", "Five", "Six"], "answer": "Three", "explanation": "Sides"},
                {"question": "Find odd: 10, 20, 30, 35", "options": ["10", "20", "30", "35"], "answer": "35", "explanation": "Not multiple of 10"},
                {"question": "If some A are B, all B are C, then?", "options": ["Some A are C", "All A are C", "No A are C", "None"], "answer": "Some A are C", "explanation": "Logic"}
            ],
            "Verbal Ability": [
                {"question": "Correct spelling:", "options": ["Accomodate", "Accommodate", "Acommodate", "Acomodate"], "answer": "Accommodate", "explanation": "Double c,m"},
                {"question": "I saw ___ elephant.", "options": ["a", "an", "the", "no article"], "answer": "an", "explanation": "Vowel sound"},
                {"question": "Opposite of 'OLD':", "options": ["Ancient", "Modern", "Historic", "Antique"], "answer": "Modern", "explanation": "Opposite"},
                {"question": "She is good ___ maths.", "options": ["in", "at", "on", "with"], "answer": "at", "explanation": "Good at"},
                {"question": "Past participle of 'WRITE':", "options": ["Wrote", "Written", "Writing", "Writes"], "answer": "Written", "explanation": "Write-Wrote-Written"},
                {"question": "Correct spelling:", "options": ["Begining", "Beginning", "Beginnig", "Begning"], "answer": "Beginning", "explanation": "Double n"},
                {"question": "He is ___ honest man.", "options": ["a", "an", "the", "no article"], "answer": "an", "explanation": "Vowel"},
                {"question": "Opposite of 'HIGH':", "options": ["Tall", "Low", "Big", "Large"], "answer": "Low", "explanation": "Opposite"},
                {"question": "They are interested ___ music.", "options": ["in", "at", "on", "with"], "answer": "in", "explanation": "Interested in"},
                {"question": "Past participle of 'GO':", "options": ["Goed", "Gone", "Went", "Going"], "answer": "Gone", "explanation": "Go-Went-Gone"}
            ],
            "Technical (CS/IT)": [
                {"question": "Which uses LIFO?", "options": ["Queue", "Stack", "Tree", "Graph"], "answer": "Stack", "explanation": "LIFO"},
                {"question": "Full form of DBMS?", "options": ["Database Management System", "Data Base Machine", "Digital Base", "Data Backup"], "answer": "Database Management System", "explanation": "DBMS"},
                {"question": "Not programming language?", "options": ["Java", "Python", "HTML", "C++"], "answer": "HTML", "explanation": "Markup"},
                {"question": "Linear search complexity?", "options": ["O(1)", "O(log n)", "O(n)", "O(n²)"], "answer": "O(n)", "explanation": "O(n)"},
                {"question": "Email protocol?", "options": ["HTTP", "FTP", "SMTP", "TCP"], "answer": "SMTP", "explanation": "SMTP"},
                {"question": "OOP language?", "options": ["C", "Java", "Assembly", "Fortran"], "answer": "Java", "explanation": "OOP"},
                {"question": "Full form of HTTP?", "options": ["HyperText Transfer Protocol", "HighText", "HyperText Transmission", "HyperText Process"], "answer": "HyperText Transfer Protocol", "explanation": "HTTP"},
                {"question": "Not data structure?", "options": ["Array", "Stack", "Compiler", "Queue"], "answer": "Compiler", "explanation": "Program"},
                {"question": "Binary search complexity?", "options": ["O(1)", "O(log n)", "O(n)", "O(n²)"], "answer": "O(log n)", "explanation": "O(log n)"},
                {"question": "File transfer protocol?", "options": ["HTTP", "FTP", "SMTP", "TCP"], "answer": "FTP", "explanation": "FTP"}
            ]
        },
        "Hard": {
            "Quantitative Aptitude": [
                {"question": "Train 60 km/h. Speed in m/s?", "options": ["16.67 m/s", "20 m/s", "15 m/s", "18 m/s"], "answer": "16.67 m/s", "explanation": "60×5/18"},
                {"question": "CP Rs.500, profit 20%, SP?", "options": ["Rs.550", "Rs.600", "Rs.650", "Rs.700"], "answer": "Rs.600", "explanation": "500+100"},
                {"question": "A:10 days, B:15 days. Together?", "options": ["5 days", "6 days", "7 days", "8 days"], "answer": "6 days", "explanation": "1/10+1/15"},
                {"question": "√0.0081?", "options": ["0.009", "0.09", "0.9", "9"], "answer": "0.09", "explanation": "√81/10000"},
                {"question": "Ratio 2:3 = ?", "options": ["4:5", "6:9", "8:10", "10:12"], "answer": "6:9", "explanation": "×3"},
                {"question": "Car 90 km/h in m/s?", "options": ["20 m/s", "25 m/s", "30 m/s", "35 m/s"], "answer": "25 m/s", "explanation": "90×5/18"},
                {"question": "SP Rs.660, profit 10%, CP?", "options": ["Rs.500", "Rs.550", "Rs.600", "Rs.650"], "answer": "Rs.600", "explanation": "660/1.1"},
                {"question": "A+B:12 days, A:20 days. B?", "options": ["25 days", "30 days", "35 days", "40 days"], "answer": "30 days", "explanation": "1/12-1/20"},
                {"question": "∛0.027?", "options": ["0.03", "0.3", "3", "30"], "answer": "0.3", "explanation": "∛27/1000"},
                {"question": "A:B=3:4, B:C=5:6. A:B:C?", "options": ["15:20:24", "3:4:6", "5:6:8", "9:12:16"], "answer": "15:20:24", "explanation": "Common B"}
            ],
            "Logical Reasoning": [
                {"question": "Missing: 2, 6, 12, 20, ?", "options": ["28", "30", "32", "36"], "answer": "30", "explanation": "+4,+6,+8,+10"},
                {"question": "5 cats, 5 mice, 5 min. 100 cats, 100 mice?", "options": ["5 min", "10 min", "50 min", "100 min"], "answer": "5 min", "explanation": "Same rate"},
                {"question": "A-B brother, C-D father, E-B mother. A-D?", "options": ["Brothers", "Uncle-Nephew", "Cousins", "Father-Son"], "answer": "Uncle-Nephew", "explanation": "Family tree"},
                {"question": "COMPUTER→DPNQVUFS. LAPTOP→?", "options": ["MBQUQP", "MBRUPQ", "MBQUQQ", "MCQUQP"], "answer": "MBQUQP", "explanation": "+1 shift"},
                {"question": "Odd pair: 2-4, 3-9, 4-16, 5-20", "options": ["2-4", "3-9", "4-16", "5-20"], "answer": "5-20", "explanation": "Should be 5-25"},
                {"question": "Missing: 3, 8, 15, 24, ?", "options": ["33", "35", "36", "40"], "answer": "35", "explanation": "+5,+7,+9,+11"},
                {"question": "3 cats, 3 mice, 3 min. 100 cats, 100 mice?", "options": ["3 min", "30 min", "100 min", "300 min"], "answer": "3 min", "explanation": "Same"},
                {"question": "A-B sister, C-D father, E-B mother. A-D?", "options": ["Sisters", "Aunt-Niece", "Cousins", "Mother-Daughter"], "answer": "Aunt-Niece", "explanation": "Family"},
                {"question": "Square:Cube :: Triangle:?", "options": ["Circle", "Pyramid", "Rectangle", "Cone"], "answer": "Pyramid", "explanation": "2D-3D"},
                {"question": "Some A are B, all B are C. Then?", "options": ["Some A are C", "All A are C", "No A are C", "None"], "answer": "Some A are C", "explanation": "Logic"}
            ],
            "Verbal Ability": [
                {"question": "One who knows everything:", "options": ["Omnipotent", "Omniscient", "Omnipresent", "Omnibus"], "answer": "Omniscient", "explanation": "All-knowing"},
                {"question": "'Break the ice' means:", "options": ["Freeze water", "Start conversation", "End friendship", "Make decision"], "answer": "Start conversation", "explanation": "Idiom"},
                {"question": "Direct: He said 'I am happy.' Indirect?", "options": ["He said that he is happy", "He said that he was happy", "He says he was happy", "He said I am happy"], "answer": "He said that he was happy", "explanation": "Reported speech"},
                {"question": "Synonym of 'CANDID':", "options": ["Secretive", "Frank", "Deceitful", "Shy"], "answer": "Frank", "explanation": "Honest"},
                {"question": "Correct spelling:", "options": ["Embarrassment", "Embarassment", "Embarasment", "Embarrasment"], "answer": "Embarrassment", "explanation": "Double r,s"},
                {"question": "One who cannot be defeated:", "options": ["Invincible", "Invisible", "Incredible", "Inevitable"], "answer": "Invincible", "explanation": "Undefeatable"},
                {"question": "'Piece of cake' means:", "options": ["Very difficult", "Very easy", "Delicious", "Expensive"], "answer": "Very easy", "explanation": "Idiom"},
                {"question": "Antonym of 'EXPAND':", "options": ["Increase", "Contract", "Grow", "Enlarge"], "answer": "Contract", "explanation": "Opposite"},
                {"question": "Synonym of 'DILIGENT':", "options": ["Lazy", "Hardworking", "Careless", "Slow"], "answer": "Hardworking", "explanation": "Same"},
                {"question": "Neither ___ suitable.", "options": ["is", "are", "were", "have been"], "answer": "is", "explanation": "Singular"}
            ],
            "Technical (CS/IT)": [
                {"question": "2 + '2' in Python?", "options": ["4", "22", "Error", "None"], "answer": "Error", "explanation": "TypeError"},
                {"question": "Not OS?", "options": ["Windows", "Linux", "Oracle", "MacOS"], "answer": "Oracle", "explanation": "Database"},
                {"question": "Uses FIFO?", "options": ["Stack", "Queue", "Tree", "Graph"], "answer": "Queue", "explanation": "FIFO"},
                {"question": "HTTP layer?", "options": ["Physical", "Data Link", "Transport", "Application"], "answer": "Application", "explanation": "Layer 7"},
                {"question": "Function keyword in Python?", "options": ["function", "def", "func", "define"], "answer": "def", "explanation": "def"},
                {"question": "Fastest sort average?", "options": ["Bubble", "Selection", "Quick", "Insertion"], "answer": "Quick", "explanation": "O(n log n)"},
                {"question": "Primary key?", "options": ["Can be null", "Uniquely identifies", "Can duplicate", "Not needed"], "answer": "Uniquely identifies", "explanation": "Unique"},
                {"question": "TCP layer?", "options": ["Physical", "Data Link", "Transport", "Application"], "answer": "Transport", "explanation": "Layer 4"},
                {"question": "Not OOP language?", "options": ["Java", "C++", "Python", "C"], "answer": "C", "explanation": "Procedural"},
                {"question": "Binary search needs?", "options": ["Unsorted", "Sorted", "Linked list", "Tree"], "answer": "Sorted", "explanation": "Sorted array"}
            ]
        }
    },
    "SY": {
        "Easy": {
            "Quantitative Aptitude": [
                {"question": "25% of 400?", "options": ["75", "100", "125", "150"], "answer": "100", "explanation": "25% of 400"},
                {"question": "Average of first 5 natural numbers?", "options": ["2", "3", "4", "5"], "answer": "3", "explanation": "15/5"},
                {"question": "SI on Rs.2000 at 5% for 2 years?", "options": ["Rs.100", "Rs.200", "Rs.300", "Rs.400"], "answer": "Rs.200", "explanation": "SI formula"},
                {"question": "7 × 8?", "options": ["54", "56", "58", "64"], "answer": "56", "explanation": "56"},
                {"question": "Rectangle: l=10, w=5. Area?", "options": ["15", "30", "50", "100"], "answer": "50", "explanation": "l×w"},
                {"question": "30% of 300?", "options": ["70", "80", "90", "100"], "answer": "90", "explanation": "90"},
                {"question": "Average of 10,20,30,40?", "options": ["20", "25", "30", "35"], "answer": "25", "explanation": "100/4"},
                {"question": "SI on Rs.3000 at 6% for 1 year?", "options": ["Rs.150", "Rs.180", "Rs.200", "Rs.220"], "answer": "Rs.180", "explanation": "180"},
                {"question": "9 × 12?", "options": ["98", "108", "118", "128"], "answer": "108", "explanation": "108"},
                {"question": "Triangle: b=10, h=8. Area?", "options": ["30", "35", "40", "45"], "answer": "40", "explanation": "½×b×h"}
            ],
            "Logical Reasoning": [
                {"question": "1,4,9,16,?", "options": ["20", "25", "30", "36"], "answer": "25", "explanation": "Squares"},
                {"question": "Odd: 3,5,7,9,11", "options": ["3", "5", "7", "9"], "answer": "9", "explanation": "Not prime"},
                {"question": "RED→TGF. BLUE→?", "options": ["CNWF", "DMXF", "DNWF", "ENXF"], "answer": "DNWF", "explanation": "+2"},
                {"question": "Yesterday Sunday. After 5 days?", "options": ["Friday", "Saturday", "Sunday", "Monday"], "answer": "Saturday", "explanation": "Mon+5"},
                {"question": "Book:Reading :: Fork:?", "options": ["Cooking", "Eating", "Kitchen", "Spoon"], "answer": "Eating", "explanation": "Analogy"},
                {"question": "2,6,12,20,?", "options": ["28", "30", "32", "36"], "answer": "30", "explanation": "+4,+6,+8,+10"},
                {"question": "Odd: 13,17,19,21,23", "options": ["13", "17", "19", "21"], "answer": "21", "explanation": "Not prime"},
                {"question": "CAT→DBU. DOG→?", "options": ["EPH", "EQH", "FPH", "EPG"], "answer": "EPH", "explanation": "+1"},
                {"question": "Today Tuesday. After 10 days?", "options": ["Wednesday", "Thursday", "Friday", "Saturday"], "answer": "Friday", "explanation": "Tue+3"},
                {"question": "Pen:Write :: Knife:?", "options": ["Sharp", "Cut", "Metal", "Kitchen"], "answer": "Cut", "explanation": "Function"}
            ],
            "Verbal Ability": [
                {"question": "Synonym of 'BEGIN':", "options": ["End", "Start", "Stop", "Finish"], "answer": "Start", "explanation": "Same"},
                {"question": "Antonym of 'HOT':", "options": ["Warm", "Cold", "Boiling", "Burning"], "answer": "Cold", "explanation": "Opposite"},
                {"question": "Plural of 'BOX':", "options": ["Boxs", "Boxes", "Boxen", "Boxies"], "answer": "Boxes", "explanation": "Add es"},
                {"question": "Past of 'EAT':", "options": ["Eated", "Eaten", "Ate", "Eating"], "answer": "Ate", "explanation": "Ate"},
                {"question": "They ___ playing.", "options": ["is", "are", "was", "been"], "answer": "are", "explanation": "Plural"},
                {"question": "Synonym of 'START':", "options": ["Begin", "End", "Stop", "Finish"], "answer": "Begin", "explanation": "Same"},
                {"question": "Antonym of 'UP':", "options": ["Top", "Down", "High", "Above"], "answer": "Down", "explanation": "Opposite"},
                {"question": "Plural of 'BUS':", "options": ["Buss", "Buses", "Busen", "Busies"], "answer": "Buses", "explanation": "Add es"},
                {"question": "Past of 'GO':", "options": ["Goed", "Gone", "Went", "Going"], "answer": "Went", "explanation": "Went"},
                {"question": "We ___ students.", "options": ["am", "is", "are", "be"], "answer": "are", "explanation": "Plural"}
            ],
            "Technical (CS/IT)": [
                {"question": "Uses LIFO?", "options": ["Queue", "Stack", "Tree", "Graph"], "answer": "Stack", "explanation": "LIFO"},
                {"question": "Full form DBMS?", "options": ["Database Management System", "Data Base Machine", "Digital Base", "Data Backup"], "answer": "Database Management System", "explanation": "DBMS"},
                {"question": "Not programming?", "options": ["Java", "Python", "HTML", "C++"], "answer": "HTML", "explanation": "Markup"},
                {"question": "Linear search?", "options": ["O(1)", "O(log n)", "O(n)", "O(n²)"], "answer": "O(n)", "explanation": "O(n)"},
                {"question": "Email protocol?", "options": ["HTTP", "FTP", "SMTP", "TCP"], "answer": "SMTP", "explanation": "SMTP"},
                {"question": "OOP language?", "options": ["C", "Java", "Assembly", "Fortran"], "answer": "Java", "explanation": "OOP"},
                {"question": "Full form HTTP?", "options": ["HyperText Transfer Protocol", "HighText", "HyperText Transmission", "HyperText Process"], "answer": "HyperText Transfer Protocol", "explanation": "HTTP"},
                {"question": "Not data structure?", "options": ["Array", "Stack", "Compiler", "Queue"], "answer": "Compiler", "explanation": "Program"},
                {"question": "Binary search?", "options": ["O(1)", "O(log n)", "O(n)", "O(n²)"], "answer": "O(log n)", "explanation": "O(log n)"},
                {"question": "File transfer?", "options": ["HTTP", "FTP", "SMTP", "TCP"], "answer": "FTP", "explanation": "FTP"}
            ]
        },
        "Medium": {
            "Quantitative Aptitude": [
                {"question": "Train 90 km/h in m/s?", "options": ["20", "25", "30", "35"], "answer": "25 m/s", "explanation": "90×5/18"},
                {"question": "SP Rs.660, profit 10%, CP?", "options": ["Rs.500", "Rs.550", "Rs.600", "Rs.650"], "answer": "Rs.600", "explanation": "660/1.1"},
                {"question": "A+B:12 days, A:20 days. B?", "options": ["25", "30", "35", "40"], "answer": "30 days", "explanation": "1/12-1/20"},
                {"question": "CI on Rs.1000 at 10% for 2 years?", "options": ["Rs.200", "Rs.210", "Rs.220", "Rs.230"], "answer": "Rs.210", "explanation": "CI=210"},
                {"question": "A:B=3:4, B:C=5:6. A:B:C?", "options": ["15:20:24", "3:4:6", "5:6:8", "9:12:16"], "answer": "15:20:24", "explanation": "Common B"},
                {"question": "Car 120 km in 2 hrs. Speed?", "options": ["50", "60", "70", "80"], "answer": "60 km/h", "explanation": "120/2"},
                {"question": "CP Rs.800, profit 15%, SP?", "options": ["Rs.880", "Rs.900", "Rs.920", "Rs.940"], "answer": "Rs.920", "explanation": "800+120"},
                {"question": "A:15 days, B:20 days. Together?", "options": ["8", "8.57", "9", "10"], "answer": "8.57 days", "explanation": "60/7"},
                {"question": "CI on Rs.2000 at 5% for 2 years?", "options": ["Rs.200", "Rs.205", "Rs.210", "Rs.215"], "answer": "Rs.205", "explanation": "CI=205"},
                {"question": "A:B=2:5, B:C=3:7. A:B:C?", "options": ["6:15:35", "2:5:7", "6:10:35", "4:10:14"], "answer": "6:15:35", "explanation": "Common B"}
            ],
            "Logical Reasoning": [
                {"question": "3,8,15,24,?", "options": ["33", "35", "36", "40"], "answer": "35", "explanation": "+5,+7,+9,+11"},
                {"question": "COMPUTER→DPNQVUFS. LAPTOP→?", "options": ["MBQUQP", "MBRUPQ", "MCQUQP", "MBQUQQ"], "answer": "MBQUQP", "explanation": "+1"},
                {"question": "A-B sister, C-D father, E-B mother. A-D?", "options": ["Sisters", "Aunt-Niece", "Cousins", "Mother-Daughter"], "answer": "Aunt-Niece", "explanation": "Family"},
                {"question": "Square:Cube :: Triangle:?", "options": ["Circle", "Pyramid", "Rectangle", "Cone"], "answer": "Pyramid", "explanation": "2D-3D"},
                {"question": "All roses flowers, some flowers fade. Then?", "options": ["All roses fade", "Some roses may fade", "No roses fade", "All flowers roses"], "answer": "Some roses may fade", "explanation": "Logic"},
                {"question": "5,12,21,32,?", "options": ["42", "44", "45", "47"], "answer": "45", "explanation": "+7,+9,+11,+13"},
                {"question": "FRIEND→HUMJTK. CANDLE→?", "options": ["EDRIRL", "DCQHQK", "EDRJKL", "FESLNM"], "answer": "EDRIRL", "explanation": "+2,+3"},
                {"question": "A-B brother, C-D sister, D-B son. A-C?", "options": ["Father", "Uncle", "Brother", "Grandfather"], "answer": "Uncle", "explanation": "Family"},
                {"question": "Circle:Sphere :: Square:?", "options": ["Rectangle", "Cube", "Triangle", "Pyramid"], "answer": "Cube", "explanation": "2D-3D"},
                {"question": "Some A are B, all B are C. Then?", "options": ["Some A are C", "All A are C", "No A are C", "None"], "answer": "Some A are C", "explanation": "Logic"}
            ],
            "Verbal Ability": [
                {"question": "Passive: He writes a letter.", "options": ["A letter is written by him", "A letter was written by him", "A letter is being written", "He is writing a letter"], "answer": "A letter is written by him", "explanation": "Present passive"},
                {"question": "'Piece of cake' means:", "options": ["Very difficult", "Very easy", "Delicious", "Expensive"], "answer": "Very easy", "explanation": "Idiom"},
                {"question": "One who cannot be defeated:", "options": ["Invincible", "Invisible", "Incredible", "Inevitable"], "answer": "Invincible", "explanation": "Undefeatable"},
                {"question": "Synonym of 'DILIGENT':", "options": ["Lazy", "Hardworking", "Careless", "Slow"], "answer": "Hardworking", "explanation": "Same"},
                {"question": "Antonym of 'EXPAND':", "options": ["Increase", "Contract", "Grow", "Enlarge"], "answer": "Contract", "explanation": "Opposite"},
                {"question": "Passive: She sings a song.", "options": ["A song is sung by her", "A song was sung by her", "A song is being sung", "She is singing a song"], "answer": "A song is sung by her", "explanation": "Present passive"},
                {"question": "'Break the ice' means:", "options": ["Freeze water", "Start conversation", "End friendship", "Make decision"], "answer": "Start conversation", "explanation": "Idiom"},
                {"question": "One who knows everything:", "options": ["Omnipotent", "Omniscient", "Omnipresent", "Omnibus"], "answer": "Omniscient", "explanation": "All-knowing"},
                {"question": "Synonym of 'BENEVOLENT':", "options": ["Cruel", "Kind", "Selfish", "Harsh"], "answer": "Kind", "explanation": "Same"},
                {"question": "Antonym of 'OPTIMISTIC':", "options": ["Hopeful", "Pessimistic", "Confident", "Positive"], "answer": "Pessimistic", "explanation": "Opposite"}
            ],
            "Technical (CS/IT)": [
                {"question": "O(n log n) average?", "options": ["Bubble", "Selection", "Quick", "Insertion"], "answer": "Quick", "explanation": "Quick sort"},
                {"question": "Primary key?", "options": ["Can be null", "Uniquely identifies", "Can duplicate", "Not needed"], "answer": "Uniquely identifies", "explanation": "Unique"},
                {"question": "TCP layer?", "options": ["Physical", "Data Link", "Transport", "Application"], "answer": "Transport", "explanation": "Layer 4"},
                {"question": "Not OOP?", "options": ["Java", "C++", "Python", "C"], "answer": "C", "explanation": "Procedural"},
                {"question": "Binary search needs?", "options": ["Unsorted", "Sorted", "Linked list", "Tree"], "answer": "Sorted", "explanation": "Sorted array"},
                {"question": "MST algorithm?", "options": ["Dijkstra", "Kruskal", "Binary Search", "Quick Sort"], "answer": "Kruskal", "explanation": "Kruskal's"},
                {"question": "HTTP stateless means?", "options": ["No errors", "Each request independent", "Very fast", "Very slow"], "answer": "Each request independent", "explanation": "No state"},
                {"question": "NoSQL database?", "options": ["MySQL", "PostgreSQL", "MongoDB", "Oracle"], "answer": "MongoDB", "explanation": "NoSQL"},
                {"question": "Inheritance means?", "options": ["Creating objects", "Reusing code", "Hiding data", "Overloading functions"], "answer": "Reusing code", "explanation": "Code reuse"},
                {"question": "Symmetric encryption?", "options": ["RSA", "AES", "ECC", "Diffie-Hellman"], "answer": "AES", "explanation": "Same key"}
            ]
        },
        "Hard": {
            "Quantitative Aptitude": [
                {"question": "P(head) in coin?", "options": ["1/4", "1/3", "1/2", "3/4"], "answer": "1/2", "explanation": "1/2"},
                {"question": "4 books arrange?", "options": ["12", "18", "24", "30"], "answer": "24", "explanation": "4!=24"},
                {"question": "2,6,12,20,30,?", "options": ["40", "42", "44", "46"], "answer": "42", "explanation": "+4,+6,+8,+10,+12"},
                {"question": "A:B=3:5, B:C=7:9. A:B:C?", "options": ["21:35:45", "3:5:9", "7:15:9", "9:15:21"], "answer": "21:35:45", "explanation": "Common B"},
                {"question": "CI Rs.2000 at 10% for 2 yrs half-yearly?", "options": ["Rs.420.50", "Rs.430.50", "Rs.440.50", "Rs.450.50"], "answer": "Rs.420.50", "explanation": "CI=420.50"},
                {"question": "P(even) in dice?", "options": ["1/6", "1/3", "1/2", "2/3"], "answer": "1/2", "explanation": "3/6"},
                {"question": "5 books arrange?", "options": ["60", "100", "120", "150"], "answer": "120", "explanation": "5!=120"},
                {"question": "1,1,2,3,5,8,?", "options": ["11", "12", "13", "15"], "answer": "13", "explanation": "Fibonacci"},
                {"question": "A:B=2:3, B:C=4:5, C:D=6:7. A:D?", "options": ["16:35", "8:35", "4:7", "2:7"], "answer": "16:35", "explanation": "Chain ratio"},
                {"question": "∛0.027?", "options": ["0.03", "0.3", "3", "30"], "answer": "0.3", "explanation": "3/10"}
            ],
            "Logical Reasoning": [
                {"question": "A 15th left, B 16th right. Swap, A 20th left. Total?", "options": ["34", "35", "36", "37"], "answer": "35", "explanation": "20+16-1"},
                {"question": "A truth 75%, B truth 80%. Both contradict?", "options": ["35%", "40%", "45%", "50%"], "answer": "35%", "explanation": "0.75×0.20+0.25×0.80"},
                {"question": "Wrong: 1,8,27,64,125,216,343,512,729,900", "options": ["512", "729", "900", "343"], "answer": "900", "explanation": "Should be 1000"},
                {"question": "'LEADER' arrange?", "options": ["360", "720", "180", "240"], "answer": "360", "explanation": "6!/2!"},
                {"question": "MONKEY→XDJMNL. TIGER→?", "options": ["QDFHS", "SDFHS", "QDEGS", "QDFGS"], "answer": "QDFHS", "explanation": "Reverse-1"},
                {"question": "A 10th left, B 12th right. Swap, A 18th left. Total?", "options": ["28", "29", "30", "31"], "answer": "29", "explanation": "18+12-1"},
                {"question": "A truth 60%, B truth 70%. Both lie?", "options": ["10%", "12%", "15%", "18%"], "answer": "12%", "explanation": "0.40×0.30"},
                {"question": "Wrong: 2,5,10,17,26,37,50,65,82,101,121", "options": ["65", "82", "101", "121"], "answer": "121", "explanation": "Should be 122"},
                {"question": "'MATHS' arrange?", "options": ["60", "100", "120", "150"], "answer": "120", "explanation": "5!"},
                {"question": "FRIEND→HUMJTK. CANDLE→?", "options": ["EDRIRL", "DCQHQK", "EDRJKL", "FESLNM"], "answer": "EDRIRL", "explanation": "+2,+3"}
            ],
            "Verbal Ability": [
                {"question": "Neither ___ suitable.", "options": ["is", "are", "were", "have been"], "answer": "is", "explanation": "Singular"},
                {"question": "Antonym of 'ZENITH':", "options": ["Peak", "Summit", "Nadir", "Top"], "answer": "Nadir", "explanation": "Opposite"},
                {"question": "Synonym of 'EPHEMERAL':", "options": ["Permanent", "Short-lived", "Eternal", "Lasting"], "answer": "Short-lived", "explanation": "Same"},
                {"question": "Fear of heights?", "options": ["Claustrophobia", "Acrophobia", "Agoraphobia", "Hydrophobia"], "answer": "Acrophobia", "explanation": "Acro=height"},
                {"question": "Each ___ a prize.", "options": ["get", "gets", "getting", "gotten"], "answer": "gets", "explanation": "Singular"},
                {"question": "Scarcely ___ arrived.", "options": ["had", "has", "have", "having"], "answer": "had", "explanation": "Inversion"},
                {"question": "Antonym of 'CACOPHONY':", "options": ["Noise", "Harmony", "Discord", "Racket"], "answer": "Harmony", "explanation": "Opposite"},
                {"question": "Synonym of 'PERNICIOUS':", "options": ["Harmless", "Harmful", "Beneficial", "Useful"], "answer": "Harmful", "explanation": "Same"},
                {"question": "Changes religion?", "options": ["Apostate", "Devotee", "Believer", "Follower"], "answer": "Apostate", "explanation": "Renounces"},
                {"question": "If I ___ you.", "options": ["am", "was", "were", "have been"], "answer": "were", "explanation": "Subjunctive"}
            ],
            "Technical (CS/IT)": [
                {"question": "Shortest path weighted graph?", "options": ["DFS", "BFS", "Dijkstra", "Binary Search"], "answer": "Dijkstra", "explanation": "Dijkstra's"},
                {"question": "Not NP-complete?", "options": ["TSP", "Knapsack", "Sorting", "Graph Coloring"], "answer": "Sorting", "explanation": "P problem"},
                {"question": "Eliminates transitive dependency?", "options": ["1NF", "2NF", "3NF", "BCNF"], "answer": "3NF", "explanation": "3NF"},
                {"question": "Not ACID?", "options": ["Atomicity", "Consistency", "Isolation", "Durability", "Concurrency"], "answer": "Concurrency", "explanation": "ACID"},
                {"question": "Public-private keys?", "options": ["AES", "DES", "RSA", "Blowfish"], "answer": "RSA", "explanation": "Asymmetric"},
                {"question": "MST algorithm?", "options": ["Dijkstra", "Kruskal", "Prim", "Both Kruskal and Prim"], "answer": "Both Kruskal and Prim", "explanation": "Both"},
                {"question": "Not P problem?", "options": ["Sorting", "Binary Search", "TSP", "Matrix Mult"], "answer": "TSP", "explanation": "NP-hard"},
                {"question": "Multi-valued dependency?", "options": ["2NF", "3NF", "4NF", "5NF"], "answer": "4NF", "explanation": "4NF"},
                {"question": "Not isolation level?", "options": ["Read Uncommitted", "Read Committed", "Repeatable Read", "Read Only"], "answer": "Read Only", "explanation": "Not isolation"},
                {"question": "Best collision resolution?", "options": ["Linear Probing", "Quadratic Probing", "Double Hashing", "Chaining"], "answer": "Chaining", "explanation": "Better"}
            ]
        }
    },
    "TY": {
        "Easy": {
            "Quantitative Aptitude": [
                {"question": "30% of 500?", "options": ["100", "125", "150", "175"], "answer": "150", "explanation": "150"},
                {"question": "Average of 20,40,60?", "options": ["30", "40", "50", "60"], "answer": "40", "explanation": "120/3"},
                {"question": "SI Rs.5000 at 8% for 3 yrs?", "options": ["Rs.1000", "Rs.1200", "Rs.1400", "Rs.1600"], "answer": "Rs.1200", "explanation": "1200"},
                {"question": "18 × 5?", "options": ["80", "85", "90", "95"], "answer": "90", "explanation": "90"},
                {"question": "Circle r=7. Area?", "options": ["144", "154", "164", "174"], "answer": "154 sq.cm", "explanation": "πr²"},
                {"question": "40% of 300?", "options": ["100", "110", "120", "130"], "answer": "120", "explanation": "120"},
                {"question": "Average of 15,25,35,45,55?", "options": ["30", "35", "40", "45"], "answer": "35", "explanation": "175/5"},
                {"question": "SI Rs.6000 at 7% for 2 yrs?", "options": ["Rs.800", "Rs.820", "Rs.840", "Rs.860"], "answer": "Rs.840", "explanation": "840"},
                {"question": "22 × 6?", "options": ["122", "132", "142", "152"], "answer": "132", "explanation": "132"},
                {"question": "Rectangle l=12,w=8. Area?", "options": ["86", "92", "96", "102"], "answer": "96 sq.cm", "explanation": "96"}
            ],
            "Logical Reasoning": [
                {"question": "100,81,64,49,?", "options": ["36", "30", "25", "20"], "answer": "36", "explanation": "10²,9²,8²,7²,6²"},
                {"question": "Odd: 17,19,23,25,29", "options": ["17", "19", "23", "25"], "answer": "25", "explanation": "Not prime"},
                {"question": "COMPUTER→DPNQVUFS. LAPTOP→?", "options": ["MBQUQP", "MBRUPQ", "MCQUQP", "MBQUQQ"], "answer": "MBQUQP", "explanation": "+1"},
                {"question": "Today Wednesday. After 10 days?", "options": ["Friday", "Saturday", "Sunday", "Monday"], "answer": "Saturday", "explanation": "Wed+3"},
                {"question": "Pen:Write :: Knife:?", "options": ["Cut", "Sharp", "Metal", "Kitchen"], "answer": "Cut", "explanation": "Function"},
                {"question": "2,6,12,20,30,?", "options": ["40", "42", "44", "46"], "answer": "42", "explanation": "+4,+6,+8,+10,+12"},
                {"question": "Odd: 31,37,41,43,45", "options": ["31", "37", "41", "45"], "answer": "45", "explanation": "Not prime"},
                {"question": "TABLE→UBCMF. CHAIR→?", "options": ["DIBJS", "DIBIR", "DJBJR", "DIBJS"], "answer": "DIBJS", "explanation": "+1"},
                {"question": "Yesterday Monday. After 15 days?", "options": ["Monday", "Tuesday", "Wednesday", "Thursday"], "answer": "Tuesday", "explanation": "Tue+1"},
                {"question": "Doctor:Hospital :: Teacher:?", "options": ["School", "Hospital", "Market", "Office"], "answer": "School", "explanation": "Workplace"}
            ],
            "Verbal Ability": [
                {"question": "Synonym of 'ACHIEVE':", "options": ["Fail", "Accomplish", "Lose", "Miss"], "answer": "Accomplish", "explanation": "Same"},
                {"question": "Antonym of 'SUCCESS':", "options": ["Victory", "Failure", "Win", "Triumph"], "answer": "Failure", "explanation": "Opposite"},
                {"question": "Plural of 'ANALYSIS':", "options": ["Analysis", "Analyses", "Analysises", "Analyseses"], "answer": "Analyses", "explanation": "Greek"},
                {"question": "Past participle of 'CHOOSE':", "options": ["Chose", "Chosen", "Choosing", "Chooses"], "answer": "Chosen", "explanation": "Choose-Chose-Chosen"},
                {"question": "The news ___ shocking.", "options": ["is", "are", "were", "have been"], "answer": "is", "explanation": "Singular"},
                {"question": "Synonym of 'COMPLETE':", "options": ["Finish", "Start", "Begin", "Continue"], "answer": "Finish", "explanation": "Same"},
                {"question": "Antonym of 'WIN':", "options": ["Victory", "Success", "Lose", "Triumph"], "answer": "Lose", "explanation": "Opposite"},
                {"question": "Plural of 'CRISIS':", "options": ["Crisis", "Crises", "Crisises", "Crisess"], "answer": "Crises", "explanation": "Greek"},
                {"question": "Past participle of 'BREAK':", "options": ["Broked", "Broke", "Broken", "Breaking"], "answer": "Broken", "explanation": "Break-Broke-Broken"},
                {"question": "The police ___ investigating.", "options": ["is", "are", "was", "been"], "answer": "are", "explanation": "Plural"}
            ],
            "Technical (CS/IT)": [
                {"question": "API stands for?", "options": ["Application Programming Interface", "Applied Program Interface", "Auto Program Integration", "Application Process Integration"], "answer": "Application Programming Interface", "explanation": "API"},
                {"question": "Cloud service model?", "options": ["IaaS", "MaaS", "DaaS", "TaaS"], "answer": "IaaS", "explanation": "IaaS"},
                {"question": "ML is subset of?", "options": ["Blockchain", "AI", "IoT", "Cloud"], "answer": "AI", "explanation": "AI"},
                {"question": "Deep learning framework?", "options": ["Django", "TensorFlow", "Flask", "Spring"], "answer": "TensorFlow", "explanation": "TensorFlow"},
                {"question": "Not OOP principle?", "options": ["Inheritance", "Polymorphism", "Compilation", "Encapsulation"], "answer": "Compilation", "explanation": "Not OOP"},
                {"question": "JSON stands for?", "options": ["JavaScript Object Notation", "Java Standard Object Notation", "JavaScript Oriented Notation", "Java Source Object Notation"], "answer": "JavaScript Object Notation", "explanation": "JSON"},
                {"question": "Not web framework?", "options": ["Django", "Flask", "Pandas", "FastAPI"], "answer": "Pandas", "explanation": "Data library"},
                {"question": "NoSQL database?", "options": ["MySQL", "PostgreSQL", "MongoDB", "Oracle"], "answer": "MongoDB", "explanation": "NoSQL"},
                {"question": "Git stands for?", "options": ["Global Information Tracker", "General Information Tool", "Global Integrated Tool", "General Integrated Tracker"], "answer": "Global Information Tracker", "explanation": "Git"},
                {"question": "Not version control?", "options": ["Git", "SVN", "Mercurial", "MySQL"], "answer": "MySQL", "explanation": "Database"}
            ]
        },
        "Medium": {
            "Quantitative Aptitude": [
                {"question": "P(head)?", "options": ["1/4", "1/3", "1/2", "3/4"], "answer": "1/2", "explanation": "1/2"},
                {"question": "4 books arrange?", "options": ["12", "18", "24", "30"], "answer": "24", "explanation": "4!"},
                {"question": "2,6,12,20,30,?", "options": ["40", "42", "44", "46"], "answer": "42", "explanation": "+4,+6,+8,+10,+12"},
                {"question": "A:B=3:5, B:C=7:9. A:B:C?", "options": ["21:35:45", "3:5:9", "7:15:9", "9:15:21"], "answer": "21:35:45", "explanation": "Common B"},
                {"question": "CI Rs.2000 at 10% for 2 yrs half-yearly?", "options": ["Rs.420.50", "Rs.430.50", "Rs.440.50", "Rs.450.50"], "answer": "Rs.420.50", "explanation": "CI=420.50"},
                {"question": "P(even)?", "options": ["1/6", "1/3", "1/2", "2/3"], "answer": "1/2", "explanation": "3/6"},
                {"question": "5 books arrange?", "options": ["60", "100", "120", "150"], "answer": "120", "explanation": "5!"},
                {"question": "1,1,2,3,5,8,?", "options": ["11", "12", "13", "15"], "answer": "13", "explanation": "Fibonacci"},
                {"question": "A:B=2:3, B:C=4:5, C:D=6:7. A:D?", "options": ["16:35", "8:35", "4:7", "2:7"], "answer": "16:35", "explanation": "Chain"},
                {"question": "∛0.027?", "options": ["0.03", "0.3", "3", "30"], "answer": "0.3", "explanation": "3/10"}
            ],
            "Logical Reasoning": [
                {"question": "5,12,21,32,?", "options": ["42", "44", "45", "47"], "answer": "45", "explanation": "+7,+9,+11,+13"},
                {"question": "FRIEND→HUMJTK. CANDLE→?", "options": ["EDRIRL", "DCQHQK", "EDRJKL", "FESLNM"], "answer": "EDRIRL", "explanation": "+2,+3"},
                {"question": "A-B brother, C-D sister, D-B son. A-C?", "options": ["Father", "Uncle", "Brother", "Grandfather"], "answer": "Uncle", "explanation": "Family"},
                {"question": "Circle:Sphere :: Square:?", "options": ["Rectangle", "Cube", "Triangle", "Pyramid"], "answer": "Cube", "explanation": "2D-3D"},
                {"question": "Some A are B, all B are C. Then?", "options": ["Some A are C", "All A are C", "No A are C", "None"], "answer": "Some A are C", "explanation": "Logic"},
                {"question": "2,5,10,17,26,?", "options": ["35", "36", "37", "38"], "answer": "37", "explanation": "+3,+5,+7,+9,+11"},
                {"question": "MONKEY→NPO LFD. TIGER→?", "options": ["UJHFS", "UIHFS", "UJGFS", "UKHFS"], "answer": "UJHFS", "explanation": "+1"},
                {"question": "A-B father, C-D brother, D-B son. A-C?", "options": ["Father", "Grandfather", "Uncle", "Brother"], "answer": "Grandfather", "explanation": "Family"},
                {"question": "Rectangle:Four :: Pentagon:?", "options": ["Four", "Five", "Six", "Seven"], "answer": "Five", "explanation": "Sides"},
                {"question": "Some A are B, some B are C. Then?", "options": ["Some A may be C", "All A are C", "No A are C", "None"], "answer": "Some A may be C", "explanation": "Possible"}
            ],
            "Verbal Ability": [
                {"question": "Passive: He writes a letter.", "options": ["A letter is written by him", "A letter was written by him", "A letter is being written", "He is writing a letter"], "answer": "A letter is written by him", "explanation": "Present passive"},
                {"question": "'Piece of cake' means:", "options": ["Very difficult", "Very easy", "Delicious", "Expensive"], "answer": "Very easy", "explanation": "Idiom"},
                {"question": "One who cannot be defeated:", "options": ["Invincible", "Invisible", "Incredible", "Inevitable"], "answer": "Invincible", "explanation": "Undefeatable"},
                {"question": "Synonym of 'DILIGENT':", "options": ["Lazy", "Hardworking", "Careless", "Slow"], "answer": "Hardworking", "explanation": "Same"},
                {"question": "Antonym of 'EXPAND':", "options": ["Increase", "Contract", "Grow", "Enlarge"], "answer": "Contract", "explanation": "Opposite"},
                {"question": "Passive: She sings a song.", "options": ["A song is sung by her", "A song was sung by her", "A song is being sung", "She is singing a song"], "answer": "A song is sung by her", "explanation": "Present passive"},
                {"question": "'Break the ice' means:", "options": ["Freeze water", "Start conversation", "End friendship", "Make decision"], "answer": "Start conversation", "explanation": "Idiom"},
                {"question": "One who knows everything:", "options": ["Omnipotent", "Omniscient", "Omnipresent", "Omnibus"], "answer": "Omniscient", "explanation": "All-knowing"},
                {"question": "Synonym of 'BENEVOLENT':", "options": ["Cruel", "Kind", "Selfish", "Harsh"], "answer": "Kind", "explanation": "Same"},
                {"question": "Antonym of 'OPTIMISTIC':", "options": ["Hopeful", "Pessimistic", "Confident", "Positive"], "answer": "Pessimistic", "explanation": "Opposite"}
            ],
            "Technical (CS/IT)": [
                {"question": "O(n log n) average?", "options": ["Bubble", "Selection", "Quick", "Insertion"], "answer": "Quick", "explanation": "Quick sort"},
                {"question": "Primary key?", "options": ["Can be null", "Uniquely identifies", "Can duplicate", "Not needed"], "answer": "Uniquely identifies", "explanation": "Unique"},
                {"question": "TCP layer?", "options": ["Physical", "Data Link", "Transport", "Application"], "answer": "Transport", "explanation": "Layer 4"},
                {"question": "Not OOP?", "options": ["Java", "C++", "Python", "C"], "answer": "C", "explanation": "Procedural"},
                {"question": "Binary search needs?", "options": ["Unsorted", "Sorted", "Linked list", "Tree"], "answer": "Sorted", "explanation": "Sorted"},
                {"question": "MST algorithm?", "options": ["Dijkstra", "Kruskal", "Binary Search", "Quick Sort"], "answer": "Kruskal", "explanation": "Kruskal's"},
                {"question": "HTTP stateless means?", "options": ["No errors", "Each request independent", "Very fast", "Very slow"], "answer": "Each request independent", "explanation": "No state"},
                {"question": "NoSQL database?", "options": ["MySQL", "PostgreSQL", "MongoDB", "Oracle"], "answer": "MongoDB", "explanation": "NoSQL"},
                {"question": "Inheritance means?", "options": ["Creating objects", "Reusing code", "Hiding data", "Overloading functions"], "answer": "Reusing code", "explanation": "Reuse"},
                {"question": "Symmetric encryption?", "options": ["RSA", "AES", "ECC", "Diffie-Hellman"], "answer": "AES", "explanation": "Same key"}
            ]
        },
        "Hard": {
            "Quantitative Aptitude": [
                {"question": "A 15th left, B 16th right. Swap, A 20th left. Total?", "options": ["34", "35", "36", "37"], "answer": "35", "explanation": "20+16-1"},
                {"question": "A truth 75%, B truth 80%. Both contradict?", "options": ["35%", "40%", "45%", "50%"], "answer": "35%", "explanation": "0.75×0.20+0.25×0.80"},
                {"question": "Wrong: 1,8,27,64,125,216,343,512,729,900", "options": ["512", "729", "900", "343"], "answer": "900", "explanation": "Should be 1000"},
                {"question": "'LEADER' arrange?", "options": ["360", "720", "180", "240"], "answer": "360", "explanation": "6!/2!"},
                {"question": "MONKEY→XDJMNL. TIGER→?", "options": ["QDFHS", "SDFHS", "QDEGS", "QDFGS"], "answer": "QDFHS", "explanation": "Reverse-1"},
                {"question": "A 10th left, B 12th right. Swap, A 18th left. Total?", "options": ["28", "29", "30", "31"], "answer": "29", "explanation": "18+12-1"},
                {"question": "A truth 60%, B truth 70%. Both lie?", "options": ["10%", "12%", "15%", "18%"], "answer": "12%", "explanation": "0.40×0.30"},
                {"question": "Wrong: 2,5,10,17,26,37,50,65,82,101,121", "options": ["65", "82", "101", "121"], "answer": "121", "explanation": "Should be 122"},
                {"question": "'MATHS' arrange?", "options": ["60", "100", "120", "150"], "answer": "120", "explanation": "5!"},
                {"question": "FRIEND→HUMJTK. CANDLE→?", "options": ["EDRIRL", "DCQHQK", "EDRJKL", "FESLNM"], "answer": "EDRIRL", "explanation": "+2,+3"}
            ],
            "Logical Reasoning": [
                {"question": "Shortest path weighted graph?", "options": ["DFS", "BFS", "Dijkstra", "Binary Search"], "answer": "Dijkstra", "explanation": "Dijkstra's"},
                {"question": "Not NP-complete?", "options": ["TSP", "Knapsack", "Sorting", "Graph Coloring"], "answer": "Sorting", "explanation": "P problem"},
                {"question": "Eliminates transitive dependency?", "options": ["1NF", "2NF", "3NF", "BCNF"], "answer": "3NF", "explanation": "3NF"},
                {"question": "Not ACID?", "options": ["Atomicity", "Consistency", "Isolation", "Durability", "Concurrency"], "answer": "Concurrency", "explanation": "ACID"},
                {"question": "Public-private keys?", "options": ["AES", "DES", "RSA", "Blowfish"], "answer": "RSA", "explanation": "Asymmetric"},
                {"question": "MST algorithm?", "options": ["Dijkstra", "Kruskal", "Prim", "Both Kruskal and Prim"], "answer": "Both Kruskal and Prim", "explanation": "Both"},
                {"question": "Not P problem?", "options": ["Sorting", "Binary Search", "TSP", "Matrix Mult"], "answer": "TSP", "explanation": "NP-hard"},
                {"question": "Multi-valued dependency?", "options": ["2NF", "3NF", "4NF", "5NF"], "answer": "4NF", "explanation": "4NF"},
                {"question": "Not isolation level?", "options": ["Read Uncommitted", "Read Committed", "Repeatable Read", "Read Only"], "answer": "Read Only", "explanation": "Not isolation"},
                {"question": "Best collision resolution?", "options": ["Linear Probing", "Quadratic Probing", "Double Hashing", "Chaining"], "answer": "Chaining", "explanation": "Better"}
            ],
            "Verbal Ability": [
                {"question": "Neither ___ suitable.", "options": ["is", "are", "were", "have been"], "answer": "is", "explanation": "Singular"},
                {"question": "Antonym of 'ZENITH':", "options": ["Peak", "Summit", "Nadir", "Top"], "answer": "Nadir", "explanation": "Opposite"},
                {"question": "Synonym of 'EPHEMERAL':", "options": ["Permanent", "Short-lived", "Eternal", "Lasting"], "answer": "Short-lived", "explanation": "Same"},
                {"question": "Fear of heights?", "options": ["Claustrophobia", "Acrophobia", "Agoraphobia", "Hydrophobia"], "answer": "Acrophobia", "explanation": "Acro=height"},
                {"question": "Each ___ a prize.", "options": ["get", "gets", "getting", "gotten"], "answer": "gets", "explanation": "Singular"},
                {"question": "Scarcely ___ arrived.", "options": ["had", "has", "have", "having"], "answer": "had", "explanation": "Inversion"},
                {"question": "Antonym of 'CACOPHONY':", "options": ["Noise", "Harmony", "Discord", "Racket"], "answer": "Harmony", "explanation": "Opposite"},
                {"question": "Synonym of 'PERNICIOUS':", "options": ["Harmless", "Harmful", "Beneficial", "Useful"], "answer": "Harmful", "explanation": "Same"},
                {"question": "Changes religion?", "options": ["Apostate", "Devotee", "Believer", "Follower"], "answer": "Apostate", "explanation": "Renounces"},
                {"question": "If I ___ you.", "options": ["am", "was", "were", "have been"], "answer": "were", "explanation": "Subjunctive"}
            ],
            "Technical (CS/IT)": [
                {"question": "Not greedy algorithm?", "options": ["Kruskal's", "Prim's", "Dijkstra's", "Bubble Sort"], "answer": "Bubble Sort", "explanation": "Not greedy"},
                {"question": "Not DP problem?", "options": ["Knapsack", "Fibonacci", "LCS", "Binary Search"], "answer": "Binary Search", "explanation": "Divide & conquer"},
                {"question": "Not B-tree property?", "options": ["All leaves same level", "Node min ceil(m/2)-1 keys", "Root min 2 children", "Keys sorted"], "answer": "Root min 2 children", "explanation": "Can have 1"},
                {"question": "Not AVL rotation?", "options": ["LL", "RR", "LR", "DD"], "answer": "DD", "explanation": "LL,RR,LR,RL"},
                {"question": "Not red-black property?", "options": ["Root black", "All leaves black", "No two reds adjacent", "All paths same black nodes"], "answer": "All leaves black", "explanation": "NIL leaves black"},
                {"question": "Not MST algorithm?", "options": ["Kruskal's", "Prim's", "Dijkstra's", "Boruvka's"], "answer": "Dijkstra's", "explanation": "Shortest path"},
                {"question": "Not comparison sort?", "options": ["Quick Sort", "Merge Sort", "Heap Sort", "Radix Sort"], "answer": "Radix Sort", "explanation": "Non-comparison"},
                {"question": "Not stable sort?", "options": ["Merge Sort", "Bubble Sort", "Insertion Sort", "Quick Sort"], "answer": "Quick Sort", "explanation": "Not stable"},
                {"question": "Not external sorting?", "options": ["Merge Sort", "External Radix", "External Quick", "Heap Sort"], "answer": "Heap Sort", "explanation": "Internal"},
                {"question": "Not divide & conquer?", "options": ["Merge Sort", "Quick Sort", "Binary Search", "Selection Sort"], "answer": "Selection Sort", "explanation": "Not D&C"}
            ]
        }
    }
}

# Initialize session state
if 'quiz_started' not in st.session_state:
    st.session_state.quiz_started = False
if 'questions' not in st.session_state:
    st.session_state.questions = []
if 'user_answers' not in st.session_state:
    st.session_state.user_answers = {}
if 'submitted' not in st.session_state:
    st.session_state.submitted = False
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'start_time' not in st.session_state:
    st.session_state.start_time = None
if 'total_attempted' not in st.session_state:
    st.session_state.total_attempted = 0
if 'total_correct' not in st.session_state:
    st.session_state.total_correct = 0

# Beautiful Header
st.markdown("""
<div style="text-align: center; padding: 20px;">
    <h1 style="font-size: 3em; color: white; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">
        🎯 Placement Prep
    </h1>
    <h2 style="color: white; font-size: 1.5em;">
        CS/IT Quiz Platform | FY to TY
    </h2>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Sidebar with beautiful design
with st.sidebar:
    st.markdown("""
    <div style="background: linear-gradient(180deg, #2C3E50 0%, #4CA1AF 100%); 
                padding: 20px; border-radius: 20px; color: white; text-align: center;">
        <h2 style="color: white;">📊 Your Progress</h2>
    </div>
    """, unsafe_allow_html=True)
    
    if st.session_state.total_attempted > 0:
        avg = (st.session_state.total_correct / (st.session_state.total_attempted * 10)) * 100
        st.metric("🎯 Quizzes Taken", st.session_state.total_attempted)
        st.metric("🏆 Average Score", f"{avg:.1f}%")
    
    if st.button("🔄 Reset Progress", use_container_width=True):
        st.session_state.total_attempted = 0
        st.session_state.total_correct = 0
        st.rerun()
    
    st.markdown("---")
    st.markdown("""
    <div style="background: white; padding: 20px; border-radius: 15px;">
        <h3 style="color: #667eea;">💡 Pro Tips</h3>
        <ul style="color: #333; line-height: 1.8;">
            <li>Start with your current year</li>
            <li>Begin with Easy, then Medium, Hard</li>
            <li>Practice all 4 categories</li>
            <li>Review explanations carefully</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Main Content
if not st.session_state.quiz_started:
    # Beautiful Selection Screen
    st.markdown("""
    <div style="background: white; padding: 40px; border-radius: 20px; 
                box-shadow: 0 10px 40px rgba(0,0,0,0.2); margin: 20px 0;">
        <h2 style="color: #667eea; text-align: center;">📋 Select Quiz Settings</h2>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style="background: white; padding: 20px; border-radius: 15px; 
                    box-shadow: 0 5px 15px rgba(0,0,0,0.1);">
            <h3 style="color: #667eea;">🎓 Year</h3>
        </div>
        """, unsafe_allow_html=True)
        year = st.selectbox(
            "",
            ["FY", "SY", "TY"],
            index=0,
            key="year_select"
        )
    
    with col2:
        st.markdown("""
        <div style="background: white; padding: 20px; border-radius: 15px; 
                    box-shadow: 0 5px 15px rgba(0,0,0,0.1);">
            <h3 style="color: #667eea;">📊 Difficulty</h3>
        </div>
        """, unsafe_allow_html=True)
        difficulty = st.selectbox(
            "",
            ["Easy", "Medium", "Hard"],
            index=0,
            key="diff_select"
        )
    
    with col3:
        st.markdown("""
        <div style="background: white; padding: 20px; border-radius: 15px; 
                    box-shadow: 0 5px 15px rgba(0,0,0,0.1);">
            <h3 style="color: #667eea;">📚 Category</h3>
        </div>
        """, unsafe_allow_html=True)
        category = st.selectbox(
            "",
            ["Quantitative Aptitude", "Logical Reasoning", "Verbal Ability", "Technical (CS/IT)"],
            index=0,
            key="cat_select"
        )
    
    num_questions = st.slider(
        "📝 Number of Questions:",
        min_value=5,
        max_value=10,
        value=10
    )
    
    st.markdown("---")
    
    # Show info
    total_available = len(QUESTION_BANKS[year][difficulty][category])
    st.info(f"📖 **{year} - {difficulty} - {category}** | Available: {total_available} questions")
    
    if st.button("🚀 Start Quiz", type="primary", use_container_width=True):
        all_questions = QUESTION_BANKS[year][difficulty][category]
        selected = random.sample(all_questions, min(num_questions, len(all_questions)))
        
        st.session_state.questions = selected
        st.session_state.user_answers = {}
        st.session_state.submitted = False
        st.session_state.score = 0
        st.session_state.quiz_started = True
        st.session_state.start_time = time.time()
        st.rerun()
    
    # Year-wise tips
    st.markdown("""
    <div style="background: white; padding: 30px; border-radius: 20px; 
                box-shadow: 0 10px 40px rgba(0,0,0,0.2); margin: 20px 0;">
        <h2 style="color: #667eea; text-align: center;">🎯 What to Expect</h2>
    </div>
    """, unsafe_allow_html=True)
    
    if year == "FY":
        st.success("""
        **FY Level Topics:**
        - Basic mathematics and calculations
        - Simple logical patterns
        - Fundamental grammar
        - Computer basics, C programming, number systems
        """)
    elif year == "SY":
        st.info("""
        **SY Level Topics:**
        - Intermediate aptitude problems
        - Complex reasoning patterns
        - Advanced grammar concepts
        - Data structures, DBMS, OS, Networks
        """)
    elif year == "TY":
        st.warning("""
        **TY Level Topics:**
        - Advanced quantitative problems
        - Critical reasoning
        - Professional communication
        - OOP, Algorithms, Cloud, ML, Security
        """)

else:
    # Quiz Screen
    st.success("📝 Quiz in Progress")
    
    if st.session_state.start_time:
        elapsed = int(time.time() - st.session_state.start_time)
        st.markdown(f"⏱️ **Time:** {elapsed//60}m {elapsed%60}s")
    
    st.markdown("---")
    
    for i, q in enumerate(st.session_state.questions):
        st.markdown(f"""
        <div style="background: white; padding: 25px; border-radius: 15px; 
                    box-shadow: 0 5px 15px rgba(0,0,0,0.1); margin: 20px 0;">
            <h3 style="color: #667eea;">Q{i+1}. {q['question']}</h3>
        </div>
        """, unsafe_allow_html=True)
        
        selected = st.radio(
            "",
            q['options'],
            key=f"q_{i}",
            index=None
        )
        
        if selected:
            st.session_state.user_answers[i] = selected
        
        st.markdown("---")
    
    if not st.session_state.submitted:
        if st.button("✅ Submit Quiz", type="primary", use_container_width=True):
            score = 0
            for i, q in enumerate(st.session_state.questions):
                if i in st.session_state.user_answers:
                    if st.session_state.user_answers[i] == q['answer']:
                        score += 1
            
            st.session_state.score = score
            st.session_state.submitted = True
            st.session_state.total_attempted += 1
            st.session_state.total_correct += score
            st.rerun()
    
    # Results
    if st.session_state.submitted:
        st.markdown("---")
        st.markdown("""
        <div style="background: white; padding: 40px; border-radius: 20px; 
                    box-shadow: 0 10px 40px rgba(0,0,0,0.2); margin: 20px 0; text-align: center;">
            <h2 style="color: #667eea; font-size: 2.5em;">🎯 Results</h2>
        </div>
        """, unsafe_allow_html=True)
        
        total = len(st.session_state.questions)
        percentage = (st.session_state.score / total) * 100
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Score", f"{st.session_state.score}/{total}")
        with col2:
            st.metric("Percentage", f"{percentage:.1f}%")
        
        st.progress(percentage / 100)
        
        if percentage >= 80:
            st.success("🌟 Excellent! You're ready!")
        elif percentage >= 60:
            st.info("👍 Good! Keep practicing!")
        else:
            st.warning("📚 Need more practice!")
        
        st.markdown("""
        <div style="background: white; padding: 30px; border-radius: 20px; 
                    box-shadow: 0 10px 40px rgba(0,0,0,0.2); margin: 20px 0;">
            <h2 style="color: #667eea; text-align: center;">📖 Solutions</h2>
        </div>
        """, unsafe_allow_html=True)
        
        for i, q in enumerate(st.session_state.questions):
            user_ans = st.session_state.user_answers.get(i, "Not answered")
            is_correct = user_ans == q['answer']
            
            with st.expander(f"Q{i+1}: {q['question']} {'✅' if is_correct else '❌'}"):
                st.write(f"**Your answer:** {user_ans}")
                st.write(f"**Correct:** {q['answer']}")
                st.info(f"💡 {q['explanation']}")
        
        st.markdown("""
        <div style="background: white; padding: 30px; border-radius: 20px; 
                    box-shadow: 0 10px 40px rgba(0,0,0,0.2); margin: 20px 0;">
            <h3 style="color: #667eea; text-align: center;">📊 Performance Tips</h3>
        </div>
        """, unsafe_allow_html=True)
        
        if percentage >= 80:
            st.success("✅ Great job! Try harder difficulty or different category!")
        elif percentage >= 60:
            st.info("👍 Good! Revise weak topics and try again!")
        else:
            st.warning("📚 Focus on basics. Try Easy difficulty first!")
        
        if st.button("🔄 New Quiz", type="primary", use_container_width=True):
            st.session_state.quiz_started = False
            st.session_state.questions = []
            st.session_state.user_answers = {}
            st.session_state.submitted = False
            st.session_state.score = 0
            st.session_state.start_time = None
            st.rerun()

# Footer
st.markdown("---")
st.markdown("""
<div style="background: white; padding: 30px; border-radius: 20px; 
            box-shadow: 0 10px 40px rgba(0,0,0,0.2); text-align: center;">
    <h3 style="color: #667eea;">🎯 Complete Coverage: FY to TY CS/IT</h3>
    <p style="color: #333; line-height: 1.8;">
        <b>Structure:</b> FY (First Year) | SY (Second Year) | TY (Third Year)<br>
        <b>Categories:</b> Quantitative Aptitude | Logical Reasoning | Verbal Ability | Technical (CS/IT)<br>
        <b>Difficulty:</b> Easy | Medium | Hard
    </p>
</div>
""", unsafe_allow_html=True)