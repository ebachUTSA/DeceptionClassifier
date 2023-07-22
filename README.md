# DeceptionClassifier
This repository holds the deception model built in support of an academic research project and resulting manuscript that explored the effects of CEO deception on analyst ratings following a cognitive load incuding situation (in this case, largely quarterly earnings calls).

Please consider citing the original work in which this model was first developed and used:

Hyde S., Bachura E., Bundy J., Greatz R., Sanders WM G., (forthcoming). The tangled webs we weave: Examining the effects of CEO deception on analyst recommendations. The Strategic Management Journal

# Using the models
Two version of the model can be found in the models directory. One of these is a scikit-learn version of the model that has been serialized
using joblib. The other version is a pytorch equivalent model that can output identical classification labels.

I have provided two sample python scripts demonstrating how to load these models. Please note that it will be necessary to load the appropriate
libraries prior to running the script.