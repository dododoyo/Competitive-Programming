class Solution {
    public boolean validMountainArray(int[] arr) {

        boolean flag1 = true,flag2 = true;

        int maxIndex = 0,max = 0;

        if (arr.length < 3)
        return false;

        for (int i = 0 ; i < arr.length ;i++)
        {
            if (arr[i] > max)
            {
                max = arr[i];
                maxIndex = i;
            }
        }

        if(maxIndex == arr.length-1 || maxIndex == 0)
        return false;

        int j =0;
        while (j < maxIndex -1 )
        {
            if (arr[j] >= arr[j+1])
            flag1 = false;
            j++;
        }

        j = maxIndex;

        if (!flag1)
        return false;

        while (j < arr.length -1 )
        {
            if (arr[j] <= arr[j+1])
            flag1 = false;
            j++;
        }

        if (flag1 && flag2)
        return true;
        else return false;

    }
}

