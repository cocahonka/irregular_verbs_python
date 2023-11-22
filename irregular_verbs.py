from typing import List;
from random import shuffle;
import os;

def readData(filePath: str) -> List[List[str]]:
    data: List[List[str]] = [];
    with open(filePath, 'r') as file:
        for line in file:
            row = list(map(lambda x: x.strip(), line.strip().split('\t')));
            data.append(row);
    
    return data;


def cls():
    os.system('cls' if os.name=='nt' else 'clear');


def removeBrackets(text: str) -> str:
    index: int = text.find('[');
    return text[:index].strip() if index != -1 else text;


def extractBracketsContent(text: str) -> str:
    start: int = text.find('[');
    end: int = text.find(']');

    return text[start+1:end] if start != -1 and end != -1 else text;


def main():
    data: List[List[str]] = readData('eng.txt');
    shuffle(data);
    
    totalQuestions: int = len(data);
    correctCount: int = 0;
    for index, row in enumerate(data):
        question: str = row[0];
        pronunciation: List[str] = list(map(extractBracketsContent,row[1:]));
        answers: List[str] = list(map(removeBrackets, row[1:]));
        
        userAnswers: List[str] = input(f'({index + 1}/{totalQuestions}) {question} > ').split();
        
        if userAnswers == answers:
            print(f'correct, pronunciation is {pronunciation}');
            correctCount += 1;
        else:
            print(f'wrong, correct answer is {answers}, and pronunciation is {pronunciation}');
        
        # hold the input
        input()
        
        cls()
      
    print(f'{correctCount} out of {totalQuestions} answered correctly');
         

if __name__ == '__main__':
    main();