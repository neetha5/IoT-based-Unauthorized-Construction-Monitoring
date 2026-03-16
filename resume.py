from resume_parser import extract_text
from matcher import match_resume

def main():
    job_file = "job_description.txt"
    
    with open(job_file, "r") as f:
        job_desc = f.read()

    resumes = ["resumes/resume1.txt", "resumes/resume2.txt"]

    for resume in resumes:
        resume_text = extract_text(resume)
        score = match_resume(resume_text, job_desc)

        print("Resume:", resume)
        print("Matching Score:", round(score * 100, 2), "%")
        print("---------------------------")

if __name__ == "__main__":
    main()