from typing import List, Tuple;
from configparser import ConfigParser;
from random import shuffle;
import os;

def readData(filePath: str) -> List[List[str]]:
    data: List[List[str]] = [];
    with open(filePath, 'r') as file:
        for line in file:
            row = list(map(lambda x: x.strip(), line.strip().split('\t')));
            data.append(row);
    
    return data;


def readConfig(filePath: str) -> Tuple[bool, bool, bool, bool]:
    config: ConfigParser = ConfigParser();
    config.read(filePath);
    
    isSecondTryEnable: bool = config.getboolean('settings', 'second_try');
    isLongWordsEnable: bool = config.getboolean('settings', 'long_words');
    isShuffleEnable: bool = config.getboolean('settings', 'shuffle');
    isCustomBoundsEnable: bool = config.getboolean('settings', 'custom_bounds');
    

    return isSecondTryEnable, isLongWordsEnable, isShuffleEnable, isCustomBoundsEnable;


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
    isSecondTryEnable, isLongWordsEnable, isShuffleEnable, isCustomBoundsEnable = readConfig('config.ini');
    
    data: List[List[str]] = readData('eng.txt');
    
    if(not isLongWordsEnable):
       data = list(filter(lambda element: len(element[1]) <= 18, data));
    
    totalQuestions: int = len(data);
    
    if(isShuffleEnable):
        shuffle(data);
    
    if(isCustomBoundsEnable):
        begin: int = int(input(f'enter the beginning of the slice [0-{totalQuestions}]: '));
        end: int = int(input(f'enter the end of the slice [0-{totalQuestions}]: '));
        data = data[begin:end];

    totalQuestions = len(data);

    wrongAnswers: List[str] = [];    
    correctCount: int = 0;
    isSecondTryUsed: bool = False;
    
    index: int = 0;
    while (index < totalQuestions):
        row: List[str] = data[index];
        question: str = row[0];
        pronunciation: List[str] = list(map(extractBracketsContent,row[1:]));
        answers: List[str] = list(map(removeBrackets, row[1:]));
        
        userAnswers: List[str] = input(f'({index + 1}/{totalQuestions}) {question} > ').split();
        
        if userAnswers == answers:
            print(f'correct, pronunciation is {pronunciation}');
            correctCount += 1;
        else:
            if (isSecondTryEnable and not isSecondTryUsed):
                print('wrong, try again');
                isSecondTryUsed = True;
                continue;

            print(f'wrong, correct answer is {answers}, and pronunciation is {pronunciation}');
            wrongAnswers.append(f'{question} - {answers} with pronunciation {pronunciation}');
        
        
        input();
        cls();
        
        index += 1;
        isSecondTryUsed = False;
      
    print(f'{correctCount} out of {totalQuestions} answered correctly');
    
    if (wrongAnswers):
        print(f'the list of words you spelled incorrectly, below are the correct answers:');
        print(*wrongAnswers, sep='\n');
         

if __name__ == '__main__':
    main();