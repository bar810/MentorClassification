import MyProject.Algorithems.CsvToDf as ReadCsv
import MyProject.Algorithems.DataPreprocessing as Preprocessing
import MyProject.Algorithems.Classifier as Classifier
import MyProject.Algorithems.Statistics as Statistics
import MyProject.Algorithems.Prediction as Prediction
pathToFile="//Path To File"


def main():
    print("Start run the program")
    # READ THE DATA-SET AND CREATE DF
    df=ReadCsv.Run(pathToFile)
    # CLEAN THE DATA, DROP UNNECESSARY ROWS AND NUMERATION
    df=Preprocessing.Run(df)
    # CREATE AND TRAIN CLASSIFIER MODEL
    classifier=Classifier.Run()
    # CHECK STATISTICS ABOUT THE MODEL
    Statistics.Run(classifier)
    # PREDICTION
    vector=[1,2,3,4,5]
    Prediction.Run(classifier,vector)
    print("Finish run the program")


