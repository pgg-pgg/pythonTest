from sklearn.feature_extraction import DictVectorizer
import csv
from sklearn import preprocessing
from sklearn import tree
from sklearn.externals.six import StringIO


#读取csv文件
allElectronicsData=open(r'/home/pgg/pythonTest/DTree/AllElectronics.csv','r')
reader=csv.reader(allElectronicsData)
header=next(reader)

featureList=[]
labelList=[]

#填充featureList（特征）和labelList（结果）
# [{'income': 'high', 'student': 'no', 'age': 'youth', 'credit_rating': 'fair'}, {'income': 'high', 'student': 'no', 'age': 'youth', 'credit_rating': 'excellent'}, {'income': 'high', 'student': 'no', 'age': 'middle_aged', 'credit_rating': 'fair'}, {'income': 'medium', 'student': 'no', 'age': 'senior', 'credit_rating': 'fair'}, {'income': 'low', 'student': 'yes', 'age': 'senior', 'credit_rating': 'fair'}, {'income': 'low', 'student': 'yes', 'age': 'senior', 'credit_rating': 'excellent'}, {'income': 'low', 'student': 'yes', 'age': 'middle_aged', 'credit_rating': 'excellent'}, {'income': 'medium', 'student': 'no', 'age': 'youth', 'credit_rating': 'fair'}, {'income': 'low', 'student': 'yes', 'age': 'youth', 'credit_rating': 'fair'}, {'income': 'medium', 'student': 'yes', 'age': 'senior', 'credit_rating': 'fair'}, {'income': 'medium', 'student': 'yes', 'age': 'youth', 'credit_rating': 'excellent'}, {'income': 'medium', 'student': 'no', 'age': 'middle_aged', 'credit_rating': 'excellent'}, {'income': 'high', 'student': 'yes', 'age': 'middle_aged', 'credit_rating': 'fair'}, {'income': 'medium', 'student': 'no', 'age': 'senior', 'credit_rating': 'excellent'}]
for row in reader:
    labelList.append(row[len(row)-1])
    rowDict={}
    for i in range(1,len(row)-1):
        rowDict[header[i]]=row[i]

    featureList.append(rowDict)

print(featureList)

#讲特征值转换为矩阵
vec=DictVectorizer()
dummyX=vec.fit_transform(featureList).toarray()
print("dummyX:"+str(dummyX))
print(vec.get_feature_names())

print("labelList:"+str(labelList))

lb=preprocessing.LabelBinarizer()
dummyY=lb.fit_transform(labelList)
print("dummyY:"+str(dummyY))

clf=tree.DecisionTreeClassifier(criterion='entropy')
clf=clf.fit(dummyX,dummyY)

print("clf:"+str(clf))


with open("allElectronicInformationGainDri.dot",'w') as f:
    f=tree.export_graphviz(clf,feature_names=vec.get_feature_names(),out_file=f)

oneRowX=dummyX[0,:].reshape(-1,10)
print("oneRowX:"+str(oneRowX))

newRowX=oneRowX

newRowX[0][0]=1
newRowX[0][2]=0

print("newRoWX:"+str(newRowX))

predictedY=clf.predict(newRowX)
print("predictedY:"+str(predictedY))