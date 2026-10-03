import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier,plot_tree



def DECISION_TREE_CLASSIFIER_PLOT(X,y,max_depth,random_state,class_names,fig_size=(20,10),feature_names =None):
    tree = DecisionTreeClassifier(max_depth=max_depth,random_state=random_state)
    tree.fit(X,y)
    plt.figure(figsize=fig_size)
    plot_tree(
        tree,
        feature_names = feature_names,
        class_names = class_names,
        filled=True,
        rounded=True
    )
    plt.show()