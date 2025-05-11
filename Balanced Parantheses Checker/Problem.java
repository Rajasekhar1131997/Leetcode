// Balanced Parantheses Checker
// This program checks if the given string has balanced parentheses, brackets, and braces.
// It uses a stack to keep track of the opening symbols and checks for matching closing symbols.
// It also handles the case where the input string is null, which would throw a NullPointerException.

import java.util.*;

public class Problem{
    public static void main(String[] args){
        String S = null;
        try {
            if (S.length() == 0) {
                System.out.println("True");
            }
        } catch (NullPointerException e) {
            System.out.println("NullPointerException found");
        }
        if (isbalanced(S)){
            System.out.println("True");
        } else {
            System.out.println("False");
        }
    }
    public static boolean isbalanced(String S){
        Stack <Character> stack = new Stack<>();
        for (int i=0;i<S.length();i++){
            if (S.charAt(i) == '(' || S.charAt(i) == '{' || S.charAt(i) == '['){
                stack.push(S.charAt(i));
            }
            else if (S.charAt(i) == ')'){
                if(stack.isEmpty() || stack.peek() != '('){
                    return false;
            }
                stack.pop();
        }
            else if (S.charAt(i) == ']') {
                if (stack.isEmpty() || stack.peek() != '['){
                    return false;
    }
                stack.pop();
            }
            else if (S.charAt(i) == '}'){
                if (stack.isEmpty() || stack.peek() != '{'){
                    return false;
                }
                stack.pop();
            }
        }
        return stack.isEmpty();
    }
}