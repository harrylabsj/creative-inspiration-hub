#!/usr/bin/env python3
"""自测脚本"""
import sys
import json
sys.path.insert(0, '..')
from handler import handle_request

def test_idea_generation():
    print("=== 测试1: 创意生成 ===")
    result = handle_request({
        "type": "idea-generation",
        "theme": "智能家居",
        "domains": ["technology", "design", "environment"]
    })
    assert result["success"] == True
    assert "ideas" in result
    assert len(result["ideas"]) == 3
    print(f"✓ 生成 {len(result['ideas'])} 个创意想法")
    print(f"  Session: {result['sessionId']}")
    print(f"  处理时间: {result['metadata']['processingTime']}ms")
    return result

def test_cross_domain():
    print("\n=== 测试2: 跨领域组合 ===")
    result = handle_request({
        "type": "cross-domain",
        "domainA": "biology",
        "domainB": "architecture",
        "applicationScenario": "可持续城市设计"
    })
    assert result["success"] == True
    assert "combinations" in result
    combo = result["combinations"][0]
    print(f"✓ 组合 {combo['domainA']} + {combo['domainB']}")
    print(f"  组合类型: {combo['combinationType']}")
    print(f"  协同效应: {combo['synergy']}")
    return result

def test_inspiration_trigger():
    print("\n=== 测试3: 灵感触发词 ===")
    result = handle_request({
        "type": "inspiration-trigger",
        "theme": "产品创新",
        "blocker": "思维定式"
    })
    assert result["success"] == True
    assert "triggers" in result
    print(f"✓ 生成 {len(result['triggers'])} 个触发词")
    for t in result["triggers"][:3]:
        print(f"  - {t['word']} (发散思维: {t['creativePotential']['divergentThinking']})")
    return result

def test_evaluation():
    print("\n=== 测试4: 创意评估 ===")
    result = handle_request({
        "type": "evaluation",
        "ideaToEvaluate": "基于区块链的二手书交易平台",
        "evaluationDimensions": ["novelty", "feasibility", "value"]
    })
    assert result["success"] == True
    assert "evaluation" in result
    eval_data = result["evaluation"]
    print(f"✓ 评估: {eval_data['idea'][:20]}...")
    print(f"  综合评分: {eval_data['scores']['overall']}/10")
    print(f"  优点: {eval_data['analysis']['strengths'][:2]}")
    return result

def test_mindmap():
    print("\n=== 测试5: 思维导图 ===")
    result = handle_request({
        "type": "mindmap",
        "coreConcept": "未来办公空间设计",
        "relatedThoughts": ["灵活工位", "健康环境", "智能协作"]
    })
    assert result["success"] == True
    assert "mindmap" in result
    mm = result["mindmap"]
    print(f"✓ 生成思维导图: {mm['title']}")
    print(f"  节点数: {mm['structure']['nodeCount']}")
    print(f"  布局: {mm['structure']['layout']}")
    return result

if __name__ == "__main__":
    print("=" * 50)
    print("Creative Inspiration Hub - 自测")
    print("=" * 50)
    try:
        test_idea_generation()
        test_cross_domain()
        test_inspiration_trigger()
        test_evaluation()
        test_mindmap()
        print("\n" + "=" * 50)
        print("✓ 所有测试通过!")
        print("=" * 50)
    except Exception as e:
        print(f"\n✗ 测试失败: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
