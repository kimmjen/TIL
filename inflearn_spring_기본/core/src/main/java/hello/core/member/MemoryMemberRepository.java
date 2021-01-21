package hello.core.member;

import java.util.HashMap;
// HashMap은 동시성 이슈가 발생, 이런경우 ConcurrentHashMap
import java.util.Map;

public class MemoryMemberRepository implements MemberRepository {

    private static Map<Long, Member> store = new HashMap<>();

    @Override
    public void save(Member member) {
        store.put(member.getId(), member);

    }

    @Override
    public Member findById(Long memberId) {
        return store.get(memberId);
    }
    
}
