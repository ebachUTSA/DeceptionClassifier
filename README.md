# DeceptionClassifier
This repository holds the deception model built in support of an academic research project and resulting manuscript that explored the effects of CEO deception on analyst ratings following a cognitive load incuding situation (in this case, largely quarterly earnings calls).

Please consider citing the original work in which this model was first developed and used:

Hyde S., Bachura E., Bundy J., Greatz R., Sanders WM G., (forthcoming). The tangled webs we weave: Examining the effects of CEO deception on analyst recommendations. The Strategic Management Journal

# Using the models
Two versions of the model can be found in the models directory. One of these is a scikit-learn version of the model that has been serialized
using joblib. The other version is a pytorch equivalent model that can output identical classification labels.

I have provided two sample python scripts demonstrating how to load these models. Please note that it will be necessary to load the appropriate
libraries prior to running the script.

These models are availalbe under are commons license that allow largely unrestricted use.

# Assumptions and Considerations for Use
I recommend reading the original paper referenced above to fully understand how this model was developed. However, in lieu of this, it is important
to understand that usage of this model carries with it some assumptions.

1) - Sufficient semantic content (model versions were all developed with a minimum of 150 words of content)
2) - Semantic content expressed in a cognitive load inducing situation. The spoken text is contextualized by a situation in which the spoken text was generated under while the speaker was necessarily using cognitive functions for that generation, e.g. - recalling events, processing new information, formulating responses dynamically.
3) - Any potential deception present in the semantic content is the result of non-trivial concerns, e.g. - there are consequences to the discovery of any potential deception that undesirable for the potential deceiver.
4) - Linguistic Inquiry Word Count values from the LIWC 2015 dictionary. These are input feature space values originally used to develop these models. See next section for more.

# Commercialized models
Improved models covering semantic, phonetic, and mixed-modality feature spaces have been developed commercially that do not require LIWC input features and have been validated in a greater range of contexts. Please contact ericbachura@arche-ai.com directly for more information.