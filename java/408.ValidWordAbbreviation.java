class Solution {
    public boolean validWordAbbreviation(String word, String abbr) {
        boolean bool = false;
        for(int i = 0, j = 0; i < word.length() && j < abbr.length();) {
            StringBuilder ch = new StringBuilder("");
            while(i < word.length() && j < abbr.length() && abbr.charAt(j) >= 'a' && abbr.charAt(j) <= 'z'){
                if (word.charAt(i) == abbr.charAt(j)) {
                    i++;
                    j++;
                } else {
                    return false;
                }

            } while((i < word.length() && j < abbr.length()) && !(abbr.charAt(j) >= 'a' && abbr.charAt(j) <= 'z')){
                ch.append( abbr.charAt(j) );
                if( ch.charAt(0) == '0') {
                    return false;
                }
                j++;
            }
            if(ch.length() > 0){
                Integer number = Integer.parseInt(ch.toString());
                
                i = i + number;
            }
            if (i == word.length() && j == abbr.length())
            { 
                bool = true;
            }
        }
        return bool;
    }
}
