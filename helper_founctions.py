class CleanData:
	def __init__(self):
		return
	def null_count(self,df):
		'''check df for nulls and return number of missing values'''
		return df.isnull().sum().sum()


def train_test_split(df, frac):
	range = len(df)
	test = df.iloc[0: round(range*frac)]
	train = df[~df.index.isin(test.index)]
	return train, test

