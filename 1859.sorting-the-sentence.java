class Solution {
    public String sortSentence(String s) 
    {
        String[] sentenceArray = s.split(" ");
        String[] sortedSentence = new String[sentenceArray.length];

        int index;
        for (String val : sentenceArray)
        {
            index = Character.getNumericValue(val.charAt((val.length()-1)));
           
            sortedSentence[index-1] = val.replace(val.charAt((val.length()-1)), ' ');
        }
        
        String theSentence="";

        for(String val: sortedSentence)
        theSentence += val;

        theSentence = theSentence.trim();
        
        return theSentence;
        
    }
}


