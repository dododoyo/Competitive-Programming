class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        targetX,targetY = target
        # distance from origin to destination
        d_frm_orgn_to_des = abs(targetX) + abs(targetY)
        for x,y in ghosts:
            # distance from origin to destination
            d_frm_ghost_to_des = abs(targetX-x) + abs(targetY-y)

            # form any of the ghost if one ghost is closer return False;
            if d_frm_orgn_to_des >= d_frm_ghost_to_des:
                return False
        return True