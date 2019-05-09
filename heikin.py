{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5/6:17.6\n",
      "5/7:17.6\n",
      "5/8:18.6\n",
      "5/9:18.2\n",
      "5/10:17.6\n",
      "5/11:18.0\n",
      "5/12:17.7\n",
      "5/13:18.4\n",
      "5/14:18.6\n",
      "5/15:19.5\n",
      "5/16:19.0\n",
      "5/17:19.4\n",
      "5/18:19.0\n",
      "5/19:19.3\n",
      "5/20:19.5\n",
      "5/21:20.1\n",
      "5/22:19.7\n",
      "5/23:19.4\n",
      "5/24:19.9\n",
      "5/25:20.4\n",
      "5/26:19.8\n",
      "5/27:19.7\n",
      "5/28:19.4\n",
      "5/29:20.5\n",
      "5/30:20.1\n",
      "5/31:20.1\n",
      "6/1:20.8\n",
      "6/2:20.5\n",
      "6/3:20.7\n",
      "6/4:20.8\n",
      "6/5:19.7\n",
      "6/6:20.4\n",
      "6/7:20.3\n",
      "6/8:20.9\n",
      "6/9:21.4\n",
      "6/10:22.2\n",
      "6/11:21.8\n",
      "6/12:21.8\n",
      "6/13:21.5\n",
      "6/14:22.4\n",
      "6/15:22.3\n",
      "6/16:21.8\n",
      "6/17:22.2\n",
      "6/18:22.2\n",
      "6/19:22.8\n",
      "6/20:22.6\n",
      "6/21:22.3\n",
      "6/22:22.7\n",
      "6/23:22.8\n",
      "6/24:23.3\n",
      "6/25:22.8\n",
      "6/26:23.5\n",
      "6/27:22.5\n",
      "6/28:23.8\n",
      "6/29:24.0\n",
      "6/30:24.1\n",
      "7/1:25.0\n",
      "7/2:25.3\n",
      "7/3:25.1\n",
      "7/4:24.6\n",
      "7/5:24.9\n",
      "7/6:24.1\n",
      "7/7:24.6\n",
      "7/8:25.1\n",
      "7/9:26.4\n",
      "7/10:26.5\n",
      "7/11:26.5\n",
      "7/12:26.8\n",
      "7/13:26.5\n",
      "7/14:26.6\n",
      "7/15:26.6\n",
      "7/16:26.7\n",
      "7/17:26.6\n",
      "7/18:27.0\n",
      "7/19:27.3\n",
      "7/20:26.8\n",
      "7/21:26.7\n",
      "7/22:26.6\n",
      "7/23:27.1\n",
      "7/24:27.4\n",
      "7/25:27.8\n",
      "7/26:27.5\n",
      "7/27:27.8\n",
      "7/28:27.4\n",
      "7/29:27.6\n",
      "7/30:27.5\n",
      "7/31:27.7\n",
      "8/1:27.6\n",
      "8/2:28.0\n",
      "8/3:27.5\n",
      "8/4:27.4\n",
      "8/5:27.7\n",
      "8/6:28.2\n",
      "8/7:28.4\n",
      "8/8:28.3\n",
      "8/9:27.1\n",
      "8/10:27.8\n",
      "8/11:27.6\n",
      "8/12:27.5\n",
      "8/13:27.6\n",
      "8/14:27.4\n",
      "8/15:27.2\n",
      "8/16:27.3\n",
      "8/17:27.1\n",
      "8/18:27.0\n",
      "8/19:27.3\n",
      "8/20:27.2\n",
      "8/21:27.6\n",
      "8/22:27.3\n",
      "8/23:26.9\n",
      "8/24:26.4\n",
      "8/25:26.6\n",
      "8/26:25.8\n",
      "8/27:25.9\n",
      "8/28:25.9\n",
      "8/29:25.5\n",
      "8/30:25.2\n",
      "8/31:24.8\n",
      "9/1:24.2\n",
      "9/2:24.7\n",
      "9/3:24.8\n",
      "9/4:24.7\n",
      "9/5:24.3\n",
      "9/6:24.1\n",
      "9/7:24.0\n",
      "9/8:23.0\n",
      "9/9:23.5\n",
      "9/10:23.9\n",
      "9/11:24.0\n",
      "9/12:23.3\n",
      "9/13:23.7\n",
      "9/14:22.8\n",
      "9/15:23.0\n",
      "9/16:22.7\n",
      "9/17:23.0\n",
      "9/18:22.7\n",
      "9/19:21.7\n",
      "9/20:21.2\n",
      "9/21:22.1\n",
      "9/22:21.8\n",
      "9/23:21.2\n",
      "9/24:21.4\n",
      "9/25:21.1\n",
      "9/26:21.3\n",
      "9/27:21.5\n",
      "9/28:21.5\n",
      "9/29:20.8\n",
      "9/30:20.0\n",
      "10/1:20.5\n",
      "10/2:20.1\n",
      "10/3:20.0\n",
      "10/4:19.2\n",
      "10/5:19.2\n",
      "10/6:19.5\n",
      "10/7:19.6\n",
      "10/8:18.9\n",
      "10/9:19.3\n",
      "10/10:19.5\n",
      "10/11:18.4\n",
      "10/12:17.7\n",
      "10/13:17.2\n",
      "10/14:17.4\n",
      "10/15:16.8\n",
      "10/16:16.7\n",
      "10/17:16.9\n",
      "10/18:16.4\n",
      "10/19:16.8\n",
      "10/20:17.4\n",
      "10/21:17.1\n",
      "10/22:17.5\n",
      "10/23:16.6\n",
      "10/24:16.2\n",
      "10/25:15.6\n",
      "10/26:15.3\n",
      "10/27:15.3\n",
      "10/28:14.9\n",
      "10/29:15.3\n",
      "10/30:14.8\n",
      "10/31:13.9\n",
      "11/1:13.7\n",
      "11/2:13.3\n",
      "11/3:12.7\n",
      "11/4:12.6\n",
      "11/5:13.4\n",
      "11/6:14.6\n",
      "11/7:15.4\n",
      "11/8:15.7\n",
      "11/9:14.8\n",
      "11/10:13.6\n",
      "11/11:13.4\n",
      "11/12:13.0\n",
      "11/13:12.1\n",
      "11/14:12.8\n",
      "11/15:11.6\n",
      "11/16:10.4\n",
      "11/17:11.0\n",
      "11/18:11.0\n",
      "11/19:11.6\n",
      "11/20:10.5\n",
      "11/21:9.9\n",
      "11/22:10.2\n",
      "11/23:9.9\n",
      "11/24:9.3\n",
      "11/25:10.3\n",
      "11/26:9.4\n",
      "11/27:9.8\n",
      "11/28:10.1\n",
      "11/29:10.0\n",
      "11/30:10.2\n",
      "12/1:9.2\n",
      "12/2:8.2\n",
      "12/3:9.5\n",
      "12/4:9.1\n",
      "12/5:8.2\n",
      "12/6:7.7\n",
      "12/7:6.6\n",
      "12/8:6.6\n",
      "12/9:6.3\n",
      "12/10:6.9\n",
      "12/11:8.0\n",
      "12/12:6.5\n",
      "12/13:6.8\n",
      "12/14:7.3\n",
      "12/15:7.0\n",
      "12/16:5.6\n",
      "12/17:4.8\n",
      "12/18:4.5\n",
      "12/19:5.7\n",
      "12/20:6.8\n",
      "12/21:6.5\n",
      "12/22:7.9\n",
      "12/23:6.6\n",
      "12/24:5.8\n",
      "12/25:5.2\n",
      "12/26:4.9\n",
      "12/27:4.7\n",
      "12/28:4.5\n",
      "12/29:4.9\n",
      "12/30:5.0\n",
      "12/31:4.2\n",
      "1/1:4.0\n",
      "1/2:4.9\n",
      "1/3:4.6\n",
      "1/4:4.8\n",
      "1/5:5.2\n",
      "1/6:4.9\n",
      "1/7:4.0\n",
      "1/8:5.5\n",
      "1/9:5.0\n",
      "1/10:4.0\n",
      "1/11:4.3\n",
      "1/12:3.8\n",
      "1/13:3.7\n",
      "1/14:3.7\n",
      "1/15:3.9\n",
      "1/16:3.8\n",
      "1/17:4.1\n",
      "1/18:4.5\n",
      "1/19:5.1\n",
      "1/20:5.7\n",
      "1/21:5.2\n",
      "1/22:4.8\n",
      "1/23:3.6\n",
      "1/24:3.0\n",
      "1/25:3.7\n",
      "1/26:3.4\n",
      "1/27:3.7\n",
      "1/28:4.8\n",
      "1/29:4.9\n",
      "1/30:5.3\n",
      "1/31:4.7\n",
      "2/1:5.6\n",
      "2/2:5.3\n",
      "2/3:5.4\n",
      "2/4:5.1\n",
      "2/5:3.9\n",
      "2/6:4.4\n",
      "2/7:4.6\n",
      "2/8:3.9\n",
      "2/9:5.1\n",
      "2/10:4.9\n",
      "2/11:4.4\n",
      "2/12:4.0\n",
      "2/13:4.6\n",
      "2/14:5.1\n",
      "2/15:5.4\n",
      "2/16:5.3\n",
      "2/17:5.7\n",
      "2/18:5.2\n",
      "2/19:5.6\n",
      "2/20:5.9\n",
      "2/21:5.3\n",
      "2/22:6.2\n",
      "2/23:7.5\n",
      "2/24:7.1\n",
      "2/25:7.5\n",
      "2/26:7.5\n",
      "2/27:7.7\n",
      "2/28:8.3\n",
      "3/1:7.9\n",
      "3/2:7.3\n",
      "3/3:6.8\n",
      "3/4:8.3\n",
      "3/5:8.8\n",
      "3/6:8.6\n",
      "3/7:8.1\n",
      "3/8:8.1\n",
      "3/9:7.8\n",
      "3/10:6.6\n",
      "3/11:6.5\n",
      "3/12:8.2\n",
      "3/13:9.0\n",
      "3/14:8.5\n",
      "3/15:8.9\n",
      "3/16:8.6\n",
      "3/17:9.7\n",
      "3/18:11.1\n",
      "3/19:11.7\n",
      "3/20:11.1\n",
      "3/21:9.2\n",
      "3/22:8.8\n",
      "3/23:9.1\n",
      "3/24:8.6\n",
      "3/25:8.5\n",
      "3/26:8.6\n",
      "3/27:9.4\n",
      "3/28:11.9\n",
      "3/29:11.9\n",
      "3/30:12.9\n",
      "3/31:11.4\n",
      "4/1:12.2\n",
      "4/2:12.5\n",
      "4/3:12.7\n",
      "4/4:11.9\n",
      "4/5:13.3\n",
      "4/6:13.3\n",
      "4/7:11.9\n",
      "4/8:12.7\n",
      "4/9:13.5\n",
      "4/10:13.1\n",
      "4/11:13.0\n",
      "4/12:12.7\n",
      "4/13:12.6\n",
      "4/14:13.5\n",
      "4/15:14.1\n",
      "4/16:15.4\n",
      "4/17:14.3\n",
      "4/18:14.4\n",
      "4/19:13.6\n",
      "4/20:13.4\n",
      "4/21:15.0\n",
      "4/22:15.2\n",
      "4/23:14.9\n",
      "4/24:15.5\n",
      "4/25:15.1\n",
      "4/26:15.8\n",
      "4/27:15.5\n",
      "4/28:15.0\n",
      "4/29:16.3\n",
      "4/30:16.8\n",
      "5/1:17.2\n",
      "5/2:17.444444444444443\n",
      "5/3:16.555555555555557\n",
      "5/4:17.11111111111111\n",
      "5/5:18.333333333333332\n",
      "2/29:4.5\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "df=pd.read_csv(\"kion10y.csv\",encoding=\"utf-8\")\n",
    "\n",
    "md={}\n",
    "for i,row in df.iterrows():\n",
    "    m,d,v=(int(row[\"月\"]),int(row[\"日\"]),int(row[\"気温\"]))\n",
    "    key=str(m)+\"/\"+str(d)\n",
    "    if not(key in md):md[key]=[]\n",
    "    md[key]+=[v]\n",
    "avs={}\n",
    "for key in md:\n",
    "    v=avs[key]=sum(md[key])/len(md[key])\n",
    "    print(\"{0}:{1}\".format(key,v))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "18.333333333333332"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "avs[\"5/5\"]"
   ]
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