{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "正解率＝ 0.9666666666666667\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/home/user/anaconda3/lib/python3.7/site-packages/sklearn/svm/base.py:196: FutureWarning: The default value of gamma will change from 'auto' to 'scale' in version 0.22 to account better for unscaled features. Set gamma explicitly to 'auto' or 'scale' to avoid this warning.\n",
      "  \"avoid this warning.\", FutureWarning)\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.svm import SVC\n",
    "from sklearn.metrics import accuracy_score\n",
    "\n",
    "iris_data=pd.read_csv(\"iris.csv\",encoding=\"utf-8\")\n",
    "\n",
    "y=iris_data.loc[:,\"Name\"]\n",
    "x=iris_data.loc[:,[\"SepalLength\",\"SepalWidth\",\"PetalLength\",\"PetalWidth\"]]\n",
    "\n",
    "x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,train_size=0.8,shuffle=True)\n",
    "\n",
    "clf=SVC()\n",
    "clf.fit(x_train,y_train)\n",
    "\n",
    "y_pred=clf.predict(x_test)\n",
    "print(\"正解率＝\",accuracy_score(y_test,y_pred))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
