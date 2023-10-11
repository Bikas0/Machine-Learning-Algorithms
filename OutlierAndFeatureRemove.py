# Outlier Detection and Replace the outlier


def remove_outlier(train_data, cols):
    for col in cols:
        q1 = train_data[col].quantile(0.25)
        print(q1)  # Read quantile value that's not necessary.
        q3 = train_data[col].quantile(0.75)
        iqr = (q3 - q1)
        upper_limit = q3 + 1.5 * iqr
        lower_limit = q1 - 1.5 * iqr
        train_data[col] = np.where(train_data[col] > upper_limit, upper_limit,
                                   np.where(train_data[col] < lower_limit, lower_limit,
                                            train_data[col]))
        # Replace outliers with NaN using np.where()
        # train_data[col] = np.where((train_data[col] < lower_limit) | (train_data[col] > upper_limit), np.nan,
        #                            train_data[col])
    return train_data


train_data = remove_outlier(train_data, features)


# Feature Remove
import seaborn as sns
#Using Pearson Correlation
plt.figure(figsize=(12,10))
cor = X_train.corr()
sns.heatmap(cor, annot=True, cmap=plt.cm.CMRmap_r)
plt.show()

# with the following function we can select highly correlated features
# it will remove the first feature that is correlated with anything other feature


def correlation(dataset, threshold):
    col_corr = set()  # Set of all the names of correlated columns
    corr_matrix = dataset.corr()
    for i in range(len(corr_matrix.columns)):
        for j in range(i):
            if abs(corr_matrix.iloc[i, j]) > threshold: # we are interested in absolute coeff value
                colname = corr_matrix.columns[i]  # getting the name of column
                col_corr.add(colname)
    return col_corr


corr_features = correlation(X_train, 0.7)
len(set(corr_features))


X_train.drop(corr_features,axis=1)
X_test.drop(corr_features,axis=1)