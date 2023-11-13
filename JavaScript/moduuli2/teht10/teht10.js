'use strict';

const numberOfCandidates = prompt("How many candidates?");
const candidatesList = [];

function Candidate(name) {
  this.name = name;
  this.votes = 0;
}

for (let i = 0; i < numberOfCandidates; i++) {
  const candidateName = prompt("Enter name of the candidate:");
  const candidate = new Candidate(candidateName);
  candidatesList.push(candidate);
}
const voters = +prompt("How many voters?");
for (let j = 0; j < voters; j++) {
  const voterChoice = prompt("Who you will vote for?");
  const selectedCandidate = candidatesList.find(function(candidate) {
    return candidate.name === voterChoice;
  });

  if (selectedCandidate) {
    selectedCandidate.votes += 1;
  } else {
    console.log("Invalid candidate name. Vote not counted.");
  }
}
let winner = candidatesList[0];
for (let candidate of candidatesList) {
  if (candidate.votes > winner.votes) {
    winner = candidate;
  }
}
candidatesList.sort((a, b) => {
   console.log(a, b);
   return b - a;
});
console.log(`The winner is ${winner.name} with ${winner.votes} votes.`);
console.log("Results:");
for (let candidate of candidatesList) {
  console.log(`${candidate.name}: ${candidate.votes} votes`);
}
