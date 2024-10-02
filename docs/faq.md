# FAQ

* **How do you know that the subproblems are non-overlapping and complete? I assume this is up to the judgment of the question-writers and the in-domain validators, but it'd be nice if there was some way of more formally confirming this (not sure that's possible though).**
  In practice, we differentiate subproblems based on their context and their role within the broader problem-solving framework (i.e. given previous subproblem-code pairs). For example, the same function for calculating a derivative could be used in different contexts: computing the force from a potential at step 3 in one main problem, and computing a velocity at step 5 in another main problem. These subproblems, although based on the same mathematical operation, are not considered overlapping because the physics and context are totally different.
 
* **SciCode doesn’t actually have other scientists try and complete the problems, so your notion of “human validation” is somewhat weak (I think the validators just look at the problems and say “yep this looks good” or “I think this is bad” with feedback)**. Ideally, we would have both in-domain and out-of-domain scientists fully engage with the problem by writing and executing the code themselves. This would allow us to systematically record their mistakes, feedback, and discussions, resulting in an ideal version of both the question design and code solution. However, given the limited capacity of our scientists pool, we need to maximize the efficiency of contributions while still achieving a high-quality validation process. Here’s what we believe is the most efficient approach:
    * **In-Domain Scientists**: In-domain scientists focus on ensuring the scientific accuracy of the problem. For each major problem, they verify that the design is sound, check the subproblem methodology, and confirm that the solution correctly reproduces published results or conforms to established theoretical models. Their expertise ensures that the scientific underpinnings of the problem are accurate.
    * **Out-of-Domain Scientists**: Out-of-domain scientists help by reviewing the question design and background information. The background is designed to augment graduate-level people who do not have specific domain expertise to successfully solve the problem. Therefore, while they may not be experts in the specific field, they can still ensure that the information provided is clear and sufficient to solve the problem.
    * **Leveraging GPT-4 for Reproduction**: Instead of requiring human scientists to reproduce the problem, we delegate this task to GPT-4. This is both cost-effective and efficient. The scientists’ primary responsibility then becomes performing error analysis on the outputs, identifying areas where the question design, solution code, or test cases may need refinement.

    This streamlined process enables us to make the most of our scientific expertise while still ensuring robust validation of the problems. By focusing human effort on critical evaluation points and using AI for reproduction tasks, we can iterate and validate problems with greater speed and precision.


* **I don’t think that SciCode validates/confirms that solutions to these problems don’t exist online.** For each main problem, our approach ensures that it reproduces results from a published paper or established theoretical model, using these references as a benchmark. This is a standard practice in scientists’ research workflow, and these benchmark results are often accessible online. 

    The challenge lies in designing specific question-code pairs that faithfully reproduce those results. These question-code pairs are either derived from our own research workflows or created from scratch for topics we consider fundamental or important to the domain.


    Take, for example, the 2D Ising model, where the transition temperature is kT/J = 2.269. While this result is easily found in this paper, reproducing it with the simulation method requires significant effort. 

    By doing so, we ensure that the problems, while based on known results, still demand an additional level of effort and insight, making them meaningful and non-trivial challenges.

* **What's the difference between the numerical tests (inputs/outputs), and “domain-specific tests”?** The difference between numerical tests (inputs/outputs) and domain-specific tests lies in how scientists assess the correctness of a problem.


    Numerical tests focus on data points, ensuring that the inputs and outputs match expected numerical values. For example, in a molecular dynamics problem, numerical tests would check the final positions and velocities of atoms under a specific potential in a closed box after some time t.


    Domain-specific tests, on the other hand, involve checking whether the solution follows the relevant physical laws or constraints. Scientists don’t just stop at numerical data; We also verify whether any physical laws are violated. In the same molecular dynamics example, apart from verifying positions and velocities, we would also check the conservation of energy and momentum. In a closed box, total energy, angular momentum, and linear momentum should remain the same before and after time t.


    The domain-specific test is a critical part of validating correctness not only for SciCode but also for real research workflows in natural science domains.




* **What were the kinds of updates made during in-domain validation?**

    During in-domain validation, all aspects of the problem can be updated to ensure accuracy and alignment with domain-specific expectations:

	* **Question Design**: Refining or rewriting the problem to better align with the desired scientific solution or to ensure clarity in how the problem is framed.
	* **Formulation of Background**: Updating the derivation or contextual background to provide a more accurate or comprehensive explanation of the problem and its relevance to the domain.
	* **Methodology**: Revising the methods used to solve the problem, which involves adjusting algorithms, simulation techniques, or approaches to ensure the solution is robust and scientifically valid.
	* **Domain-specific Tests**: Updating the domain-specific checks that validate the fundamental physical laws or constraints.

    At this stage, we have even totally rewritten a couple of problems to ensure that the question design can be properly paired with the code, making the problem-solving process more effective and scientifically rigorous.



* **How can I trust the out-of-domain validation?**
    The role of out-of-domain validation is not to ensure scientific correctness but rather to verify that the problem is presented in a way that is clear, complete, and accessible to someone outside the specific field. The primary focus of out-of-domain validators is to ensure that the combination of the question and its background information provides enough context for someone to solve the problem, even if they lack domain-specific expertise.



* **It seems that in the prompt template definition, the prompts with and without backgrounds are assigned the other way around:
  DEFAULT_PROMPT_TEMPLATE = Path("eval", "data", "background_comment_template.txt").read_text()
  BACKGOUND_PROMPT_TEMPLATE = Path("eval", "data", "multistep_template.txt").read_text()
Are the numbers reported in the paper run with these prompts?**

    Yes, DEFAULT_PROMPT_TEMPLATE is our standard setup where we ask the model to generate the related background itself. BACKGOUND_PROMPT_TEMPLATE is the template where we will put in the scientist-annotated background.



* **For subproblems 13.6, 62.1, 76.2, it seems like the model-generated outputs are ignored and replaced with the files in the eval folder - is this how the evaluations were run in the paper? And why are these problems evaluated this way?**
    These three problem-code pairs are provided as given context in order to control uncertainty and reduce the degrees of freedom in the evaluation process. By doing so, we limit the model’s randomness in problem-solving. Without this context, the evaluation would allow for too many possible solutions, leading to inconsistent results.



* **In line 66, if self.previous_llm_code[prev_step] is None the previous steps are populated with saved model outputs after running them through extract_function_name and get_function_from_code; otherwise the previous steps are populated with extract_python_script. It doesn't seem like the first case is invoked except for the subproblems 13.6, 62.1, 76.2 - can you confirm that extract_python_script was used for the numbers in the paper?**
    This setup is designed specifically to handle cases where the model is interrupted mid-step and needs to resume from that point.
