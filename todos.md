Todos:

Rishabh:

* Set up travis CI

Arvi:

* Set up README.md

Group Todos:

* we need to generally classify stages of the conversation and then come up with a set of possible responses a person might give - If the conversation gets too far off topic we need to be able to redirect the topic to the type of conversation we are comfortable having

The states of the conversation:

From the perspective of the victim / trafficker:

1) greeting - this has been mocked out - we need to get this fully fleshed out.
2) flirting - dropping hints that the girl is under aged, willing and able.  If possible, we should try not to be overt, because this might spoke potiential users of the system.  Unless they are overt first.

For this reason we need to have two types of flirting and we need to be able to detect to two types of flirting:

Overt and submissive flirting

3) Setting up the deal - we need to notice when the deal is being set up and be able to respond appropriately.

4) Setting up the drop - we need to be able to notice when the drop point is being set.

5) redirecting the conversation - we need to be able to redirect the conversation for when things are being taken in a different direction.

From the perspective of the police officer / under cover

1) greeting - this has been mocked out - we need to get this fully fleshed out.
2) flirting - dropping hints that the girl is under aged, willing and able.  If possible, we should try not to be overt, because this might spoke potiential users of the system.  Unless they are overt first.

For this reason we need to have two types of flirting and we need to be able to detect to two types of flirting:

Overt and submissive flirting

3) Setting up the deal - we need to notice when the deal is being set up and be able to respond appropriately.

4) Setting up the drop - we need to be able to notice when the drop point is being set.

5) redirecting the conversation - we need to be able to redirect the conversation for when things are being taken in a different direction.

Here we need to do generally the same things, however this will be the other side of the conversation, so we'll build this out as needed as well.


How this will work in practice:

1) we'll need to build up a set of text for classification for understanding when we are in each part of the conversation as well as logic for understanding when we've moved from one part of the conversation to the next.  We also need to be able to understand when conversations move backward in the process or forward.  We'll call this "arguing".

2) we'll make use of the database to inform the training data for the classifiers - I'm going to recommend svm's for this however, feel free to use whatever you find most useful.  I'm going to recommend spacy, but nltk is good to.  Scikit learn has the best svm implementation, so we should use that no matter what nlp interface is decided on.


