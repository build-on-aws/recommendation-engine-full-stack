## Full Stack Recommendation Engine 

Sample code repo that forms the base of the following tutorial:
* [Build Your Own Recommendation Engine for a Streaming Platform Clone on AWS: A Full Stack Tutorial](https://buildon.aws/tutorials/recommendation-engine-full-stack)
* Detailed setup and steps are provided in the tutorial.
* Explanation of the folders that you see in this repo
    * infrastructure folder
        * Cloudformation tenplates that build teh resources for the tutorial
    * data folder
        * Contains  the python notebook, the raw csv movie files , kmeans output from previous iterations to save time and the localui folder has the User Interface for our fancy MyFlix UI
    * sagemaker-migration-toolkit
        * Utility code to make deployment of  custom scaling model on sagemaker easier
    * apis_for_sagemaker_models
        * There are 2 folders containing the snippets of code for creating our REST API using the [Chalice framework](https://github.com/aws/chalice)



## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.

